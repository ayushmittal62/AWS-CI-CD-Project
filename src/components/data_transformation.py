import numpy as np
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
# from src.components.data_ingestion import 
import os
import sys
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_col = ["writing_score", "reading_score"]
            categorical_col = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("Scalar", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("One_ot Encoding", OneHotEncoder()),
                    ("Standard Scalar", StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Numerical featres standard scaling done: {numerical_col}")
            logging.info(f"Categorical features encoding done: {categorical_col}")

            preprocessor = ColumnTransformer(
                [
                    ("Numecial Features", num_pipeline, numerical_col),
                    ("Categorical Features", cat_pipeline, categorical_col)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Data read Done - Both Train and Test Data")

            preprocessor_object = self.get_data_transformer_object()
            target_column_name = "math_score"
            numerical_colums = ["reading_score", "writing_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            
            target_feature_train_df = train_df[target_column_name]
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying the preprocessor data on traing and testing data")

            input_feature_train_arr = preprocessor_object.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_object.transform(input_feature_test_df)

            # Concatenate features and targets
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]


            logging.info("saved Preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_object
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)