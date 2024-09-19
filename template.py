# Importing the Modules
import os
import sys
from pathlib import Path

# List of file paths to be created
list_of_files = [
    "requirements.txt",
    "setup.py",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/pipelines/__init__.py",
    "src/pipelines/training_pipeline.py",
    "src/pipelines/prediction_pipeline.py",
    "src/utils.py",
    "artifacts/.gitkeep",
    "notebooks/trials.ipynb",
    "src/logger.py",
    "src/exception.py"
]


# Iterate through each file path in the list
for file_path in list_of_files:

    # Convert string file path to a Path object for easy handling
    file_path = Path(file_path)

    # Split the file path into directory and file name
    file_dir, file_name = os.path.split(file_path)

    # Create the directory if it does not exist
    if file_dir != "":
        # Create the directory if it doesn't exist, 'exist_ok=True' prevents errors if it already exists
        os.makedirs(file_dir,exist_ok=True)

    # Check if the file either doesn't exist or its size is 0 (i.e., it's empty)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):

        print(f"File {file_path} is empty or does not exist")
        # Create the file (or empty it if it already exists) by opening in write mode
        with open(file_path,"w") as f:
            pass
