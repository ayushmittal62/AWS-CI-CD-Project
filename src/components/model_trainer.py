import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import(AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor)
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model    

@dataclass
class ModelTrainingConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def  __init__(self):
        self.model_trainer_config = ModelTrainingConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting Training and Test input data")

            X_train, Y_train = train_array[:, :-1], train_array[:, -1]
            X_test, Y_test = test_array[:, :-1], test_array[:, -1]


            models = {
                    "Linear Regression": LinearRegression(),
                    "Ridge" : Ridge(),
                    "KNeighborsRegressor" : KNeighborsRegressor(),
                    "Decision Tree" : DecisionTreeRegressor(),
                    "Random Forest" : RandomForestRegressor(),
                    "CatBoostRegressor" :  CatBoostRegressor(verbose=False),
                    "AdaBoost Regressor" : AdaBoostRegressor(),
                    "Gradient Boosting" : GradientBoostingRegressor()
                    }
            
            model_report:dict = evaluate_model(X_train = X_train,Y_train = Y_train,X_test = X_test, Y_test = Y_test,
                                                models = models)
            
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No Best Model Found")
            
            logging.info("best model found on both training and testing data")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj= best_model
            )

            predicted = best_model.predict(X_test)
            r2_scoore = r2_score(Y_test, predicted)
            return r2_scoore
            

        except Exception as e:
            raise CustomException(e, sys)
