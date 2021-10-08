from e2eml.regression import regression_blueprints as rb
import pandas as pd
from sklearn.metrics import mean_absolute_error
# track memory consumption in terminal: dmesg


def load_housingprices_data():
    """
    Load & preprocess Housing prices dataset. T
    :return: Several dataframes and series to be processed by blueprint.
    """
    data = pd.read_csv("housingprices_train.csv")

    def new_features(X):
        X['HasWoodDeck'] = (X['WoodDeckSF'] == 0) * 1
        X['HasOpenPorch'] = (X['OpenPorchSF'] == 0) * 1
        X['HasEnclosedPorch'] = (X['EnclosedPorch'] == 0) * 1
        X['Has3SsnPorch'] = (X['3SsnPorch'] == 0) * 1
        X['HasScreenPorch'] = (X['ScreenPorch'] == 0) * 1
        X['Total_Home_Quality'] = X['OverallQual'] + X['OverallCond']
        X['TotalSF'] = X['TotalBsmtSF'] + X['1stFlrSF'] + X['2ndFlrSF']
        X['TotalSquareFootage'] = (X['BsmtFinSF1'] + X['BsmtFinSF2'] + X['1stFlrSF'] + X['2ndFlrSF'])
        X['HasPool'] = X['PoolArea'].apply(lambda x: 1 if x > 0 else 0)
        X['Has2ndFloor'] = X['2ndFlrSF'].apply(lambda x: 1 if x > 0 else 0)
        X['HasGarage'] = X['GarageArea'].apply(lambda x: 1 if x > 0 else 0)
        X['HasBsmt'] = X['TotalBsmtSF'].apply(lambda x: 1 if x > 0 else 0)
        X['HasFireplace'] = X['Fireplaces'].apply(lambda x: 1 if x > 0 else 0)
        return X

    data = new_features(data)
    print('Do dataframe splits.')
    test_df = data.head(1000).copy()
    val_df = data.tail(460).copy()
    val_df_target = val_df["SalePrice"].copy()
    del val_df["SalePrice"]
    test_target = "SalePrice"
    test_categorical_cols = ["MSZoning", "Street", "Alley", "LotShape", "LotFrontage", "Street", "LandContour",
                             "Utilities", "LotConfig", "LandSlope", "Neighborhood", "Condition1", "Condition2",
                             "BldgType", "HouseStyle", "RoofStyle", "RoofMatl", "Exterior1st", "Exterior2nd",
                             "ExterQual", "ExterCond", "Foundation", "BsmtQual", "BsmtCond", "BsmtExposure",
                             "BsmtFinType1", "BsmtFinType2", "Heating", "HeatingQC", "Electrical", "KitchenQual",
                             "Functional", "FireplaceQU", "GarageType", "GarageYrBlt", "GarageFinish", "GarageQual",
                             "GarageCond", "PavedDrive", "PoolQC", "Fence", "MiscFeature", "SaleType", "SaleCondition"]
    return test_df, test_target, val_df, val_df_target, test_categorical_cols


def test_ml_special_regression_multiclass_full_processing_multimodel_avg_blender():
    test_df, test_target, val_df, val_df_target, test_categorical_cols = load_housingprices_data()
    titanic_auto_ml = rb.RegressionBluePrint(datasource=test_df,
                                   target_variable=test_target,
                                   categorical_columns=test_categorical_cols,
                                   preferred_training_mode='auto',
                                             tune_mode='accurate')
    titanic_auto_ml.hyperparameter_tuning_rounds = {"xgboost": 3,
                                                    "lgbm": 3,
                                                    "tabnet": 3,
                                                    "ngboost": 3,
                                                    "sklearn_ensemble": 3,
                                                    "ridge": 3,
                                                    "bruteforce_random": 10}
    titanic_auto_ml.special_blueprint_algorithms = {"ridge": True,
                                                    "xgboost": True,
                                                    "ngboost": True,
                                                    "lgbm": True,
                                                    "tabnet": False,
                                                    "vowpal_wabbit": False,
                                                    "sklearn_ensemble": False
                                                    }

    titanic_auto_ml.ml_special_regression_full_processing_multimodel_avg_blender()
    titanic_auto_ml.ml_special_regression_full_processing_multimodel_avg_blender(val_df)
    val_y_hat = titanic_auto_ml.predicted_values['blended_preds']
    mae = mean_absolute_error(val_df_target, val_y_hat)
    finished = True
    assert mae < 30000, finished == True


def test_ml_bp10_train_test_regression_full_processing_linear_reg():
    test_df, test_target, val_df, val_df_target, test_categorical_cols = load_housingprices_data()
    titanic_auto_ml = rb.RegressionBluePrint(datasource=test_df,
                                             target_variable=test_target,
                                             categorical_columns=test_categorical_cols,
                                             preferred_training_mode='auto',
                                             tune_mode='accurate')
    titanic_auto_ml.ml_bp10_train_test_regression_full_processing_linear_reg()
    titanic_auto_ml.ml_bp10_train_test_regression_full_processing_linear_reg(val_df)
    val_y_hat = titanic_auto_ml.predicted_values['linear_regression']
    mae = mean_absolute_error(val_df_target, val_y_hat)
    finished = True
    assert finished == True


