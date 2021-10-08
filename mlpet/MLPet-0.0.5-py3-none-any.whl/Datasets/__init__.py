import os
import yaml
import warnings
import joblib
import numpy as np
import pandas as pd
import importlib
import operator
import warnings

from . import helpers
from . import feature_helpers
from . import imputation_helpers

from cognite.client import CogniteClient

import sklearn.preprocessing

class Dataset(object):
    """    
    The main class representing a dataset

    Attributes
    ----------
        settings: dict
            the required keys for the dictionary:
                'type': which subclass the settings belong to (required for the high-level API only and needs to follow a specific format),
                'file_name': pickled filename (not the full path) to read the data from, or dump the data to,
                'curves': list of features from the raw data to use,
                'id_column': name of the id column,
                'label_column': name of the column containing the labels,
                'num_filler': filler value for numerical curves(existing or wishing value for replacing missing values),
                'cat_filler': filler value categorical curves(existing or wishing value for replacing missing values),
                'scaler_method': (options: 'StandardScaler', 'RobustScaler'),
                'gradient_features': whether to calculate gradients of features (boolean),
                'window_features': whether to calculate rolling aggregations (min, max, mean) of features (boolean),
                'window': size of the rolling window for calculating the window features (int),
                'log_features': whether to add log of every feature as a new feature (boolean)
        *all setting keys are also set as class attributes

        folder_path: the path to the local copy of the data as well as the serialized scaler and imputer(if applicable)

    Methods
    -------
        load_from_cdf(client:CogniteClient, reload:bool)
            - loads data from CDF and dumps it in folder_path/file_name if reload=True
            - loads data from folder_path/file_name if reload=False
            - populates the 'df_original' attribute

        load_from_csv(filepath:str)
            - loads local data from filepath into the 'df_original' attribute

        load_from_pickle(filepath:str)
            - loads local data from filepath into the 'df_original' attribute

        load_from_dict(filepath:str)
            - loads local data from filepath into the 'df_original' attribute

        preprocess(train:bool)
            - performs all preprocessing according to the settings
            - splits data into train and test set (if train=True)
            - saves scaler and imputer to folder_path/scaler.joblib and folder_path/imputer.joblib (if applicable)
                or loads them from the mentioned paths to use for preprocessing
    """

    def __init__(self, mappings, settings, folder_path):

        def _ingest_input(att_name, att_val):
            if isinstance(att_val, dict):
                setattr(self, att_name, att_val)
            elif isinstance(att_val, str):
                if os.path.isfile(att_val):
                    att_path = '{}_path'.format(att_name)
                    setattr(self, att_path, att_val)
                    with open(getattr(self, att_path)) as file:
                        setattr(self, att_name, yaml.load(file, Loader=yaml.FullLoader))

        self.folder_path = folder_path
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)

        _ingest_input(att_name='settings', att_val=settings)
        for key, val in self.settings.items():
            setattr(self, key, val)

        _ingest_input(att_name="mappings", att_val=mappings)
        if 'curve_mappings' in self.mappings.keys():
            self.curve_mappings = self.mappings['curve_mappings']
        if 'formations_map' in self.mappings.keys():
            self.formations_map = self.mappings['formations_map']
        if 'groups_map' in self.mappings.keys():
            self.groups_map = self.mappings['groups_map']

        # Fill in any possible gaps in settings
        if not hasattr(self, 'curves_to_scale'):
            setattr(self, 'curves_to_scale', [])

        if not hasattr(self, 'lognames'):
            setattr(self, 'lognames', [])
        
        if not hasattr(self, 'log_features'):
            setattr(self, 'log_features', [])

        if not hasattr(self, 'gradient_features'):
            setattr(self, 'gradient_features', [])

        if not hasattr(self, 'window'):
            self.window = 1

        if not hasattr(self, 'noise_removal_window'):
            self.noise_removal_window = None

        if not hasattr(self, 'feat_eng'):
            self.feat_eng = None
        
        if not hasattr(self, 'drop_original_curves'):
            self.drop_original_curves = False

        if not hasattr(self, 'scaler_method'):
            self.scaler_method = 'RobustScaler'

        if not hasattr(self, 'num_filler'):
            self.num_filler = 0

        if not hasattr(self, 'cat_filler'):
            self.cat_filler = 'MISSING'

        if not hasattr(self, 'curves_to_normalize'):
            warnings.warn('"curves_to_normalize" not provided in dataset settings. Note that you are NOT normalizing "GR", make sure this is intentional!')
            setattr(self, 'curves_to_normalize', [])

        # Standardize the provided curve names
        for attr in ['curves', 'curves_to_scale', 'curves_to_normalize', 'gradient_features', 'log_features']:
            setattr(self, '{}_original'.format(attr), getattr(self, attr))
            setattr(self, attr, helpers._standardize_names(names=getattr(self, attr), mapper=self.curve_mappings))

        # Check that the label curve is not present in the curves
        if self.label_column in self.curves:
            raise ValueError (f'Label column ({self.label_column}) is present in the input curves.')

        # Check that curves_to_scale is a  subset of curves
        for attr in ['curves_to_scale']:
            all_curves = set(getattr(self, 'curves'))
            sub_curves = set(getattr(self, attr))
            if not sub_curves.issubset(all_curves): 
                raise ValueError ('{} is not a subset of curves {}'.format(attr, getattr(self, 'curves')))

        if hasattr(self, 'imputer'):
            self.imputer_path = os.path.join(self.folder_path, 'imputer.joblib')
        else:
            self.imputer = None

        self.scaler_path = os.path.join(self.folder_path, 'scaler.joblib')
        self.data_path   = os.path.join(self.folder_path, self.file_name)

    def _read_data(self):
        """
        Identify column type and checks all expected curves are present
        """
        self._validate_data()

    def load_from_cdf(self, client:CogniteClient, reload=False):
        """                
        Loads and validates data
        
        Args:
            client: CogniteClient for authentication
            reload: boolean - default False
                if reload is True: downloads data from CDF as a pandas DataFrame and saves model_path/file_name as in Dataset settings
                if reload is False: expects pickled file to exist at model_path/file_name, otherwise loads it from CDF
        """
        self.df_original = self._load_data_faster(client, reload=reload)
        self._read_data()

    def load_from_csv(self, filepath, **kwargs):
        """
        Loads data from csv files and validates data

        Args:
            filepath (string): path to csv file
        """
        self.df_original = pd.read_csv(filepath, **kwargs)
        self._read_data()

    def load_from_pickle(self, filepath, **kwargs):
        """
        Loads data from pickle file and validates

        Args:       
            filepath (string): path to pickle file
        """
        self.df_original = pd.read_pickle(filepath, **kwargs)
        self._read_data()

    def load_from_dict(self, data_dict):
        """
        Loads data from a dictionary and validates it

        Args:
            data_dict (string): dictionary with data
        """
        self.df_original = pd.DataFrame.from_dict(data_dict)
        self._read_data()

    def load_from_df(self, data_df):
        """
        Loads data from dataframe and validates it

        Args:
            data_df (pandas.Dataframe): dataframe with data
        """
        self.df_original = data_df
        self._read_data()

    def train_test_split(self, test_size=0.2, df=None, **kwargs):
        """
        Splits a dataset into training and val/test sets.
        **kwargs: test_size and test_wells (if applicable) 
        
        Args:
            test_size (float, optional): percentage of data to be test set. Defaults to 0.2.
            df (pd.DataFrame, optional): dataframe with data. Defaults to None.

        Returns:
            tuple: dataframes for train and test sets, and list of test wells IDs
        """
        if df is None:
            df = self.df_original
        df = self._drop_rows_wo_label(df, **kwargs)
        return helpers._df_split_train_test(df, self.id_column, test_size=test_size, **kwargs)

    def feature_target_split(self, df, **kwargs):
        """
        Splits set into features and target

        Args:
            df (pd.DataFrame): dataframe to be split

        Returns:
            tuple: input (features) and output (target) dataframes
        """
        df = helpers._standardize_curve_names(df, mapper=kwargs.get('curve_mappings', self.curve_mappings))
        if self.id_column not in self.curves:
            X = df.loc[:, ~df.columns.isin([self.label_column, self.id_column])]
        else:
            X = df.loc[:, ~df.columns.isin([self.label_column])]
        y = df[self.label_column]
        return X, y

    def preprocess(self, df, **kwargs):
        """
        Main preprocess function, including all required steps by the user

        Args:
            df (pd.Dataframe): dataframe to which apply preprocessing

        Returns:
            pd.Dataframe: preprocessed dataframe
            dictionary: key wells and values for each curve
            list: feats_to_keep specifies which curves should be kept in accordance to the settings file
        """
        
        # identify categorical and numerical curves, impute if needed
        df, num_cols, cat_cols = helpers._apply_metadata(df, **kwargs.get('_metadata', {}))
        # standardize curve names
        df = helpers._standardize_curve_names(df, mapper=kwargs.get('curve_mappings', self.curve_mappings))
        # remove or clip values in some curves
        df = helpers._remove_cutoff_values(df, self.curves)
        # impute value with depth trend
        df = imputation_helpers._impute_depth_trend(df, self.folder_path, **kwargs.get('_depth_trend_imputation', {}))
        # remove noise if chosen
        if self.noise_removal_window is not None:
            df = self._remove_noise(df, cols=list(num_cols))
        # generate specified features if chosen
        if self.feat_eng is not None:
            df = self._feature_engineer(df)
        # normalize some curves 
        df, key_wells = self._normalize_curves(df, **kwargs.get('_normalize_curves', {}))
        # preprocess whole dataset (including add features to the dataset)
        df, added_cols = self._preprocess(df, **kwargs.get('_preprocess', {}))
        
        # preprocess some curves per well
        if self.id_column in df.columns:
            well_names = df[self.id_column].unique()
            res_df     = pd.DataFrame()
            time_cols  = None
            for well in well_names:
                well_df                            = df.loc[df[self.id_column]==well, :].copy()
                well_df, new_cols, curves_to_scale = self._process_well(well_df, **kwargs.get('_process_well', {}))
                if 'time_features' in kwargs.keys():
                    time_cols   = [c for c in df.columns if c != self.id_column and c != self.label_column]
                    well_df, time_cols = feature_helpers._add_time_features(well_df, tim_cols, kwargs['time_features'])
                res_df = res_df.append(well_df)
            df = res_df.copy()
            curves_to_scale = curves_to_scale + time_cols if time_cols!=None else curves_to_scale
        else:
            df, new_cols, curves_to_scale = self._process_well(df, **kwargs.get('_process_well', {}))
            warnings.warn('Not possible to process per well as well ID is not in dataset. Preprocessing was done considering all data is from the same well.')
        
        # fill the missing Z_LOC values with regards to DEPTH_MD(always present)
        if ("Z_LOC" in self.curves) and ("DEPTH_MD" in self.curves):
            df.loc[:, 'Z_LOC'] = df['Z_LOC'].fillna(-(df['DEPTH_MD'] - 20))
        # impute missing rows
        num_cols, cat_cols  = helpers._make_col_dtype_lists(df)
        df.loc[:, num_cols] = df[num_cols].fillna(self.num_filler)
        df.loc[:, cat_cols] = df[cat_cols].fillna(self.cat_filler)

        # map the categorical features
        df = self._encode_columns(df, columns=cat_cols)
        # drop original values if chosen otherwise all columns will be considered
        feats_to_keep = list(df.columns)
        if self.drop_original_curves:
            to_drop = self.log_features + self.gradient_features
            # we have to add here to drop the curves generated for time features from the original
            if 'time_features' in kwargs.keys():
                time_cols_drop = []
                for t in range(1, kwargs['time_features']+1):
                    time_cols_drop = time_cols_drop + [f'{c}_{t}' for c in to_drop]
                to_drop = to_drop + time_cols_drop
            feats_to_keep = [c for c in df.columns if c not in to_drop]
        

        # make sure we only have numerical features to scale
        num_feats       = set(df[feats_to_keep]._get_numeric_data().columns)
        curves_to_scale = list(set(curves_to_scale) & num_feats)
        # scale columns globally
        if len(curves_to_scale) > 0:
            df.loc[:, curves_to_scale] = self._scale_columns(
                df, 
                columns=curves_to_scale, 
                scaler_method=self.scaler_method, 
                **kwargs
            )      
        
        added_cols = added_cols + new_cols
        self.added_features = added_cols

        return df, key_wells, feats_to_keep

    def _feature_engineer(self, df):
        """
        Creates features the user specifies from features of the original dataset. If the value of the feature is 1,
        it will be added to curves to scale.

        Args:
            df (pd.DataFrame): dataframe to which add features from and to

        Returns:
            pd.DataFrame: dataframe with added features
        """
        if ('VPVS' in self.feat_eng.keys()):
            if (set(['AC', 'ACS']).issubset(set(df.columns))):
                df.loc[:, 'VPVS'] = df['ACS']/df['AC']
                if 'VPVS' not in self.curves:
                    self.curves.append('VPVS')
                if self.feat_eng['VPVS']==1:
                    self.curves_to_scale.append('VPVS')
            else:
                raise ValueError('Not possible to generate VPVS as both necessary curves (AC and ACS) are not present in dataset.')
            
        if ('PR' in self.feat_eng.keys()):
            if not (set(['VP', 'VS']).issubset(set(df.columns))):
                if (set(['AC', 'ACS']).issubset(set(df.columns))):
                    df['VP']   = 304.8/df['AC']
                    df['VS']   = 304.8/df['ACS']
                else:
                    raise ValueError('Not possible to generate PR as none of the neccessary curves (AC, ACS or VP, VS) are present in the dataset.')
            df.loc[:, 'PR'] = (df['VP']**2 - 2.0 * df['VS']**2) / (2.0 * (df['VP']**2 - df['VS']**2))
            if 'PR' not in self.curves:
                self.curves.append('PR')
            if self.feat_eng['PR']==1:
                self.curves_to_scale.append('PR')

        if ('RAVG' in self.feat_eng.keys()):
            r_curves = [c for c in ['RDEP', 'RMED', 'RSHA'] if c in df.columns]
            if len(r_curves)>1:
                df.loc[:, 'RAVG'] = df[r_curves].mean(axis=1)
                if 'RAVG' not in self.curves:
                    self.curves.append('RAVG')
                if self.feat_eng['RAVG']==1:
                    self.curves_to_scale.append('RAVG')
            else:
                raise ValueError('Not possible to generate RAVG as there is only one or none resistivities curves in dataset.')
            
        if 'LFI' in self.feat_eng.keys():
            if (set(['NEU', 'DEN']).issubset(set(df.columns))):
                df.loc[:, 'LFI'] = 2.95-((df['NEU']+0.15)/0.6)- df['DEN']
                df.loc[df['LFI']<-0.9,'LFI'] = 0
                df['LFI'] = df['LFI'].fillna(0)
                if 'LFI' not in self.curves:
                    self.curves.append('LFI')
                if self.feat_eng['LFI']==1:
                    self.curves_to_scale.append('LFI')
            else:
                raise ValueError('Not possible to generate LFI as NEU and/or DEN are not present in dataset.')
    
        if 'FI' in self.feat_eng.keys():
            if 'LFI' in df.columns:
                df.loc[:, 'FI'] = (abs(df['LFI'])+df['LFI'])/2
            elif (set(['NEU', 'DEN']).issubset(set(df.columns))):
                df.loc[:, 'LFI'] = 2.95-((df['NEU']+0.15)/0.6)- df['DEN']
                df.loc[df['LFI']<-0.9,'LFI']=0
                df.loc[:, 'LFI'] = df['LFI'].fillna(0)
                df.loc[:, 'FI']  = (abs(df['LFI'])+df['LFI'])/2
            else:
                raise ValueError('Not possible to generate FI as NEU and/or DEN are not present in dataset.')
            if 'FI' not in self.curves:
                self.curves.append('FI')
            if self.feat_eng['FI']==1:
                self.curves_to_scale.append('FI')

        if 'LI' in self.feat_eng.keys():
            if 'LFI' in df.columns:
                df.loc[:, 'LI']=abs(abs(df['LFI'])-df['LFI'])/2 
            elif (set(['NEU', 'DEN']).issubset(set(df.columns))):
                df.loc[:, 'LFI'] = 2.95-((df['NEU']+0.15)/0.6)- df['DEN']
                df.loc[df['LFI']<-0.9,'LFI']=0
                df.loc[:, 'LFI'] = df['LFI'].fillna(0)
                df.loc[:, 'LI']  = abs(abs(df['LFI'])-df['LFI'])/2 
            else:
                raise ValueError('Not possible to generate LI as NEU and/or DEN are not present in dataset.')
            if 'LI' not in self.curves:
                self.curves.append('LI')
            if self.feat_eng['LI']==1:
                    self.curves_to_scale.append('LI')

        if ('AI' in self.feat_eng.keys()):
            if (set(['DEN', 'AC']).issubset(set(df.columns))):
                df.loc[:, 'AI'] = df['DEN']*((304.8/df['AC'])**2)
                if 'AI' not in self.curves:
                    self.curves.append('AI')
                if self.feat_eng['AI']==1:
                    self.curves_to_scale.append('AI')
            else:
                raise ValueError('Not possible to generate AI as DEN and/or VP are not present in the dataset.')

        if ('CALI-BS' in self.feat_eng.keys()):
            if 'CALI' in df.columns:
                if 'BS' not in df.columns:
                    df = helpers._guess_BS_from_CALI(df)
                    if 'BS' not in self.curves:
                        self.curves.append('BS')
                df, diff_cols = feature_helpers._add_inter_curves(df, curves=['CALI', 'BS'], new_col_name='CALI-BS', method='sub')
                if 'CALI-BS' not in self.curves:
                    self.curves.append('CALI-BS')
                if self.feat_eng['CALI-BS']==1:
                    self.curves_to_scale.append('CALI-BS')
            else:
                raise ValueError('Not possible to generate CALI-BS. At least CALI needs to be present in the dataset.')

        return df

    def _validate_data(self):
        """
        Checks that the data loaded into the Dataset includes the expected curves
        """
        # check that all expected curves are present in the data
        expected_curves = self.curves
        present_curves  = self.df_original.columns.tolist()
        expected_but_missing_curves = [c for c in expected_curves if c not in present_curves]
        if expected_but_missing_curves:
            warnings.warn("Warning...........There are curves that are expected but missing from data. They are being filled with num_filler {}".format(expected_but_missing_curves))
            self.df_original[expected_but_missing_curves] = self.num_filler

    def _encode_columns(self, df, columns=None):
        """
        Encodes categorical columns. Only available for certain categorical values at the moment.

        Args:
            df (pd.DataFrame): dataframe to which apply encoding of categorical variables
            columns (list): which columns to encode. Deafults to None.
        
        Returns:
            pd.DataFrame: dataframe with categorical columns encoded
        """   
        if columns is None:
            columns = self.cat_columns
        if 'FORMATION' in columns:
            df['FORMATION'] = df['FORMATION'].map(self.formations_map)

        if 'GROUP' in columns:
            df['GROUP'] = df['GROUP'].map(self.groups_map)

        if 'lsuName' in columns:
            df['lsuName'] = df['lsuName'].map(self.groups_map)

        return df

    def _filter_curves(self, df, curves=None):
        """
        Returns a dataframe with only curves chosen by user, filtered from the original dataframe

        Args:
            df (pd.DataFrame): dataframe to filter
            curves (list, optional): which curves should be kept. Defaults to None.

        Returns:
            pd.DataFrame: dataframe with relevant curves
        """
        if curves is None:
            curves = self.curves
        try:
            curves_to_keep = self.curves + [self.label_column] 
            if not self.id_column in curves_to_keep:
                curves_to_keep = curves_to_keep + [self.id_column]
            return df.loc[:, curves_to_keep]
        except KeyError:
            return df.loc[:, self.curves]

    def _normalize_curves(self, df, **kwargs):
        """
        Normalizes dataframe columns.
        We choose one well to be a "key well" and normalize all other wells to its low and high values.
        If the user provides key wells, keys wells calculation is not perfomed.

        Args:
            df (pd.DataFrame): dataframe with columns to normalize

        Returns:
            tuple: pd.DataFrame with normalized values and dictionary with key wells and values
        """
        low_perc       = kwargs.get('low_perc', 0.05)
        high_perc      = kwargs.get('high_perc', 0.95)
        user_key_wells = kwargs.get('key_wells')
        save_key_wells = kwargs.get('save_key_wells', False)
        
        if user_key_wells is None:
            wells_data = df.groupby(self.id_column)
            key_wells  = {c: None for c in self.curves_to_normalize}
            for c in self.curves_to_normalize:
                low_p  = wells_data[c].quantile(low_perc)
                high_p = wells_data[c].quantile(high_perc)

                # get the key well with largest difference between limit values
                key_well = (high_p-low_p).idxmax()

                df.loc[:, 'low_p']  = df[self.id_column].map(low_p)
                df.loc[:, 'high_p'] = df[self.id_column].map(high_p)
                # save the key wells for normalization
                key_wells[c] = {
                    'curve': c,
                    'well_name': key_well,
                    'ref_low': df[df[self.id_column]==key_well]['low_p'].unique()[0],
                    'ref_high': df[df[self.id_column]==key_well]['high_p'].unique()[0]
                }
                # normalize all other wells
                df.loc[:, c] = df.apply(
                    lambda x: helpers._normalize(
                        x[c],
                        key_wells[c]['ref_low'],
                        key_wells[c]['ref_high'],
                        x['low_p'],
                        x['high_p'],
                        ),
                        axis=1
                        )
        else:
            # if key wells is provided as a dict with the same format
            if isinstance(user_key_wells, dict):
                if user_key_wells.keys() != set(self.curves_to_normalize):
                    raise ValueError(
                        "Curves included in the key wells dictionary incosistent with curves_to_normalize", 
                        user_key_wells.key(), self.curves_to_normalize)
                else:
                    key_wells = user_key_wells
                    for c in self.curves_to_normalize:
                        df.loc[:, 'low_p']  = key_wells[c]['ref_low']
                        df.loc[:, 'high_p'] = key_wells[c]['ref_high']
                        # normalize all other wells
                        df.loc[:, c] = df.apply(
                            lambda x: helpers._normalize(
                                x[c],
                                key_wells[c]['ref_low'],
                                key_wells[c]['ref_high'],
                                x['low_p'],
                                x['high_p'],
                                ),
                                axis=1
                                )
            else:
                ValueError("Other methods to provide key wells are not implemented yet!") 
        
        if save_key_wells:                          
            # save key wells to where model is
            joblib.dump(key_wells, os.path.join(self.folder_path, 'key_wells.joblib'))
        return df, key_wells

    def _preprocess(self, df, **kwargs):
        """
        Preprocessing pipeline for all wells, independently of well ID

        Args:
            df (pd.DataFrame): dataframe to preprocess

        Returns:
            tuple: preprocessed dataframe and columns that were added, if any
        """
        # filter relevant curves
        df = self._filter_curves(df)
        # add features
        added_cols = []
        # add feature log10
        if len(self.log_features)>0:
            df, log_cols = feature_helpers._add_log_features(df, self.log_features)
            added_cols   = added_cols + log_cols
        return df, added_cols

    def _scale_columns(self, df, columns, scaler_method='RobustScaler', **kwargs):
        """
        Scales specified columns

        Args:
            df (pd.DataFrame): dataframe containing columns to scale
            columns (list): list with columns to scale
            scaler_method (str, optional): scaling method. Defaults to 'RobustScaler'.

        Returns:
            pd.DataFrame: scaled columns
        """
        cls_name = scaler_method
        try:
            cls = getattr(sklearn.preprocessing, cls_name)
        except AttributeError as ae:
            print(ae)
        self.scaler = cls(**kwargs.get('scaler', {}))
        self.scaler.fit(df[columns])
        # save scaler to same path as model
        scaler_path = os.path.join(self.folder_path, 'scaler.joblib')
        joblib.dump(self.scaler, scaler_path)
        return self.scaler.transform(df[columns])

    def _process_well(self, df, **kwargs):
        """
        Process specific well: imputation, features creation (rolling, gradient)

        Args:
            df (pd.DataFrame): dataframe of one well

        Returns:
            tuple: processed dataframe of well, added columns names, curves to scale list
        """
        # impute features
        if self.imputer == 'iterative':
            df = imputation_helpers._iterative_impute(df)
        if self.imputer == 'simple':
            df = imputation_helpers._simple_impute(df)

        added_cols = []
        # add rolling features
        if self.window_features:
            rolling_columns, _ = helpers._make_col_dtype_lists(df[self.curves])
            df.loc[:, self.curves], window_cols = feature_helpers._add_rolling_features(df, rolling_columns, self.window)
            added_cols = added_cols + window_cols

        # add gradient features
        if self.gradient_features:
            df.loc[:, self.curves], gradient_cols = feature_helpers._add_gradient_features(df, self.gradient_features)
            added_cols = added_cols + gradient_cols

        # add the created features to curves_to_scale, if the original ones are also in curves_to_scale,
        # including the logs that were generated for the whole data
        feats_to_add = []
        for col in self.curves_to_scale:
            feats_to_add = feats_to_add + [c for c in df.columns if col+'_' in c]
            
        # scale_features
        curves_to_scale = self.curves_to_scale + feats_to_add

        return df, added_cols, curves_to_scale

    def _remove_noise(self, df, cols):
        """
        Removes noise by applying a median filter in each curve

        Args:
            df (pd.DataFrame): dataframe to which apply median filtering
            cols (list): list of column to apply noise removal with median filter

        Returns:
            pd.DataFrame: dataframe after removing noise
        """
        cols     = [c for c in cols if c != 'DEPTH']
        df.loc[:, cols] = df[cols].rolling(
            self.noise_removal_window,
            center=True,
            min_periods=1
            ).median()
        return df

    def _drop_rows_wo_label(self, df, **kwargs):
        """
        Removes columns with missing targets.
        Now that the imputation is done via pd.df.fillna(), what we need is the constant filler_value
        If the imputation is everdone using one of sklearn.impute methods or a similar API, we can use 
        the indicator column (add_indicator=True)

        Args:
            df (pd.DataFrame): dataframe to process

        Returns:
            pd.DataFrame: processed dataframe
        """
        filler_value = kwargs.get('filler_value', None)
        if filler_value is not None:
            return df.loc[df[self.label_column]!=filler_value, :]
        else:
            return df.loc[~df[self.label_column].isna(), :]