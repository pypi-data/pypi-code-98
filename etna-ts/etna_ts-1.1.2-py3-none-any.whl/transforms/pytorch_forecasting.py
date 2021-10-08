import inspect
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

import pandas as pd
from pytorch_forecasting.data import TimeSeriesDataSet
from pytorch_forecasting.data.encoders import EncoderNormalizer
from pytorch_forecasting.data.encoders import NaNLabelEncoder
from pytorch_forecasting.data.encoders import TorchNormalizer
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

from etna.datasets.tsdataset import TSDataset
from etna.transforms.base import Transform

NORMALIZER = Union[TorchNormalizer, NaNLabelEncoder, EncoderNormalizer]


class PytorchForecastingTransform(Transform):
    """Transform for models from PytorchForecasting library."""

    def __init__(
        self,
        max_encoder_length: int = 30,
        min_encoder_length: int = None,
        min_prediction_idx: int = None,
        min_prediction_length: int = None,
        max_prediction_length: int = 1,
        static_categoricals: List[str] = [],
        static_reals: List[str] = [],
        time_varying_known_categoricals: List[str] = [],
        time_varying_known_reals: List[str] = [],
        time_varying_unknown_categoricals: List[str] = [],
        time_varying_unknown_reals: List[str] = [],
        variable_groups: Dict[str, List[int]] = {},
        dropout_categoricals: List[str] = [],
        constant_fill_strategy: Dict[str, Union[str, float, int, bool]] = {},
        allow_missings: bool = True,
        lags: Dict[str, List[int]] = {},
        add_relative_time_idx: bool = True,
        add_target_scales: bool = True,
        add_encoder_length: Union[bool, str] = True,
        target_normalizer: Union[NORMALIZER, str, List[NORMALIZER], Tuple[NORMALIZER]] = "auto",
        categorical_encoders: Dict[str, NaNLabelEncoder] = None,
        scalers: Dict[str, Union[StandardScaler, RobustScaler, TorchNormalizer, EncoderNormalizer]] = {},
    ):
        """Parameters for TimeSeriesDataSet object.

        Notes
        -----
        This transform should be added at the very end of `transforms` parameter.

        Reference
        ---------
        https://github.com/jdb78/pytorch-forecasting/blob/v0.8.5/pytorch_forecasting/data/timeseries.py#L117
        """
        super().__init__()
        self.max_encoder_length = max_encoder_length
        self.min_encoder_length = min_encoder_length
        self.min_prediction_idx = min_prediction_idx
        self.min_prediction_length = min_prediction_length
        self.max_prediction_length = max_prediction_length
        self.static_categoricals = static_categoricals
        self.static_reals = static_reals
        self.time_varying_known_categoricals = time_varying_known_categoricals
        self.time_varying_known_reals = time_varying_known_reals
        self.time_varying_unknown_categoricals = time_varying_unknown_categoricals
        self.time_varying_unknown_reals = time_varying_unknown_reals
        self.variable_groups = variable_groups
        self.add_relative_time_idx = add_relative_time_idx
        self.add_target_scales = add_target_scales
        self.add_encoder_length = add_encoder_length
        self.allow_missings = allow_missings
        self.target_normalizer = target_normalizer
        self.categorical_encoders = categorical_encoders
        self.dropout_categoricals = dropout_categoricals
        self.constant_fill_strategy = constant_fill_strategy
        self.lags = lags
        self.scalers = scalers

    @staticmethod
    def _calculate_freq_unit(freq: str) -> pd.Timedelta:
        """Calculate frequency unit by its string representation."""
        if freq[0].isdigit():
            return pd.Timedelta(freq)
        else:
            return pd.Timedelta(1, unit=freq)

    def fit(self, df: pd.DataFrame) -> "PytorchForecastingTransform":
        """
        Fit TimeSeriesDataSet.

        Parameters
        ----------
        df:
            data to be fitted.

        Returns
        -------
            PytorchForecastingTransform
        """
        self.freq = pd.infer_freq(df.index)
        ts = TSDataset(df, self.freq)
        df_flat = ts.to_pandas(flatten=True)
        df_flat = df_flat.dropna()
        self.min_timestamp = df_flat.timestamp.min()

        if self.time_varying_known_categoricals:
            for feature_name in self.time_varying_known_categoricals:
                df_flat[feature_name] = df_flat[feature_name].astype(str)

        freq_unit = self._calculate_freq_unit(self.freq)
        df_flat["time_idx"] = (df_flat["timestamp"] - self.min_timestamp) / freq_unit
        df_flat["time_idx"] = df_flat["time_idx"].astype(int)

        pf_dataset = TimeSeriesDataSet(
            df_flat,
            time_idx="time_idx",
            target="target",
            group_ids=["segment"],
            time_varying_known_reals=self.time_varying_known_reals,
            time_varying_known_categoricals=self.time_varying_known_categoricals,
            time_varying_unknown_reals=self.time_varying_unknown_reals,
            max_encoder_length=self.max_encoder_length,
            max_prediction_length=self.max_prediction_length,
            min_encoder_length=self.min_encoder_length,
            min_prediction_length=self.min_prediction_length,
            add_relative_time_idx=self.add_relative_time_idx,
            add_target_scales=self.add_target_scales,
            add_encoder_length=self.add_encoder_length,
            allow_missings=self.allow_missings,
            target_normalizer=self.target_normalizer,
            static_categoricals=self.static_categoricals,
            min_prediction_idx=self.min_prediction_idx,
            variable_groups=self.variable_groups,
            dropout_categoricals=self.dropout_categoricals,
            constant_fill_strategy=self.constant_fill_strategy,
            lags=self.lags,
            scalers=self.scalers,
        )

        self.pf_dataset_params = pf_dataset.get_parameters()

        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Transform raw df to TimeSeriesDataSet.

        Parameters
        ----------
        df:
            data to be transformed.

        Returns
        -------
            DataFrame

        Notes
        -----
        We save TimeSeriesDataSet in instance to use it in the model.
        It`s not right pattern of using Transforms and TSDataset.
        """
        ts = TSDataset(df, self.freq)
        df_flat = ts.to_pandas(flatten=True)
        df_flat = df_flat[df_flat.timestamp >= self.min_timestamp]
        df_flat = df_flat.fillna(0)

        freq_unit = self._calculate_freq_unit(self.freq)
        df_flat["time_idx"] = (df_flat["timestamp"] - self.min_timestamp) / freq_unit
        df_flat["time_idx"] = df_flat["time_idx"].astype(int)

        if self.time_varying_known_categoricals:
            for feature_name in self.time_varying_known_categoricals:
                df_flat[feature_name] = df_flat[feature_name].astype(str)

        if inspect.stack()[1].function == "make_future":
            pf_dataset_predict = TimeSeriesDataSet.from_parameters(
                self.pf_dataset_params, df_flat, predict=True, stop_randomization=True
            )
            self.pf_dataset_predict = pf_dataset_predict
        else:
            pf_dataset_train = TimeSeriesDataSet.from_parameters(self.pf_dataset_params, df_flat)
            self.pf_dataset_train = pf_dataset_train
        return df
