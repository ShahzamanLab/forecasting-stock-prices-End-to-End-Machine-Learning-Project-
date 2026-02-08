import os
from pathlib import Path

list_of_files = [
## Main Project FILES

    "Data/raw",
    "Data/preprocessed",
    "src/__init__.py",
    "src/config.py",
    "src/Data_loader.py",
    "src/Data_preprocessing.py",
    "src/model.py",
    "src/train.py",
    "src/predict.py",
    "notebook/exploration.ipynb",
    "models/",
    "Test/test.py",
    "Test/test.ipynb",
    "requirements.txt",
    "app.py",

    ## Automation Files for the Project

    "automation_pipeline/pipeline_core/__init__.py",
    "automation_pipeline/pipeline_core/data_loader.py",
    "automation_pipeline/pipeline_core/data_preprocessing.py",
    "automation_pipeline/pipeline_core/feature_engineering.py",
    "automation_pipeline/pipeline_core/model_selection.py",
    "automation_pipeline/pipeline_core/train_pipeline.py",
    "automation_pipeline/pipeline_core/evaluate.py",
    "automation_pipeline/pipeline_core/predict_pipeline.py",
    "automation_pipeline/pipeline_core/main_pipeline.py"



]

for file_path in list_of_files:
    path = Path(file_path)
    folder = path.parent
    if folder != Path("."):
        os.makedirs(folder, exist_ok=True)
    if path.suffix:  
        path.touch(exist_ok=True)
