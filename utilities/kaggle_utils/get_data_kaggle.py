def get_data_kaggle_competition(folder_to_save, competition_name):
    """
    Download and extract a Kaggle competition dataset in Python.
    Deletes the zip file after extraction to save space.
    
    Parameters
    ----------
    folder_to_save : str or pathlib.Path
        Folder where the dataset will be saved.
    competition_name : str
        Exact name of the Kaggle competition.
    """
    from pathlib import Path
    import zipfile
    import kaggle
    import os

    # Make sure is a real path
    folder_to_save = Path(folder_to_save)
    
    # Crate the directory
    if folder_to_save.is_dir():
        print(f"{folder_to_save} directory exists.")
    else:
        print(f"Did not find {folder_to_save} directory, creating...")
        folder_to_save.mkdir(parents=True, exist_ok=True)

    # Download 

    print(f"Downloading {competition_name} into {folder_to_save}...")
    kaggle.api.competition_download_files(competition_name, path=str(folder_to_save))
    
    # Make the new .zip
    zip_file = folder_to_save / f"{competition_name}.zip"

    # unzip + delete

    if zip_file.exists():
        print(f"Extracting {zip_file}...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(folder_to_save)
        print("Extraction complete.")

        # Remove zip
        os.remove(zip_file)
        print(f"Deleted zip file {zip_file} to save space.")
    else:
        print(f"Error: {zip_file} not found. Check if download was successful.")

    print("Downloaded and extracted files:", list(folder_to_save.iterdir()))
