import os
from pathlib import Path

list_of_files = [
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
]

for file_path in list_of_files:
    path = Path(file_path)
    folder = path.parent
    if folder != Path("."):
        os.makedirs(folder, exist_ok=True)
    if path.suffix:  
        path.touch(exist_ok=True)
