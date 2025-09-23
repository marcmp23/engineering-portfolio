def get_data_kaggle_competition(folder_to_save, competition_name):
    """
    Download and extract a Kaggle competition dataset in Google Colab.
    
    Parameters
    ----------
    folder_to_save : str or pathlib.Path
        Folder where the dataset will be saved.
    competition_name : str
        Exact name of the Kaggle competition 
        
    """
    
    from pathlib import Path
    import zipfile
    import kaggle
    # Create just in case

    if folder_to_save.is_dir():
        print(f"{folder_to_save} directory exists.")
    else:
        print(f"Did not find {folder_to_save} directory, creating...")
        folder_to_save.mkdir(parents=True, exist_ok=True)


        # Download data
        kaggle competitions download -c competition_name -p folder_to_save

        # unzip
        zip_file = folder_to_save / competition_name/ ".zip"
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(folder_to_save)

        print("Downloaded:", list(folder_to_save.iterdir()))



