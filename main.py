import argparse
import kaggle

def upload_dataset(dataset_path, version_notes):
    """
    Upload a dataset to Kaggle.

    Parameters:
        dataset_path (str): The path to the dataset directory. This directory should contain all dataset files and the dataset-metadata.json file.
        version_notes (str): Notes about the dataset version being uploaded.
    """

    #  Reference: https://www.kaggle.com/code/donkeys/kaggle-python-api
    kaggle.api.dataset_create_version(
        folder=dataset_path, 
        version_notes=version_notes, 
        quiet=False, 
        convert_to_csv=False, 
        delete_old_versions=False, 
        dir_mode='skip'
    )

def main():
    parser = argparse.ArgumentParser(description="Upload a dataset to Kaggle.com")
    parser.add_argument("dataset_path", type=str, help="Path to the directory containing the dataset and dataset-metadata.json files")
    parser.add_argument("version_notes", type=str, help="Version notes for the dataset being uploaded")

    args = parser.parse_args()

    upload_dataset(args.dataset_path, args.version_notes)

if __name__ == "__main__":
    main()
