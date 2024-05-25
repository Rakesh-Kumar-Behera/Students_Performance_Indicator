from src.utils import save_object
from src.utils import evaluate_models

from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation_obj = DataTransformation()
    train_arr,test_arr,_ = data_transformation_obj.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))