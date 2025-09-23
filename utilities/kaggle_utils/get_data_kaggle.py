def get_data_kaggle_competition(folder_to_save, competition_name):
    """
    Download and extract a Kaggle competition dataset in Google Colab.

    Parameters
    ----------
    folder_to_save : str or pathlib.Path
        The path to the folder where the dataset will be saved.
    competition_name : str
        The exact name of the Kaggle competition (e.g., "alzheimers-disease-risk-prediction-eu-business").

    Workflow
    --------
    1. Creates the folder if it does not exist.
    2. Installs the Kaggle Python package if not installed.
    3. Prompts the user to upload their `kaggle.json` token file.
    4. Places the token in `~/.kaggle/` and sets secure permissions.
    5. Downloads the competition dataset using the Kaggle CLI.
    6. Extracts all ZIP files in the target folder.
    7. Prints the list of downloaded files.
    
    Notes
    -----
    - This function is designed for Google Colab.
    - The user must have a valid Kaggle account and token.
    """
    
    from pathlib import Path
    import zipfile

    folder_to_save = Path(folder_to_save)

    # Step 1: Create folder if it does not exist
    if folder_to_save.is_dir():
        print(f"{folder_to_save} directory exists.")
    else:
        print(f"Did not find {folder_to_save} directory, creating...")
        folder_to_save.mkdir(parents=True, exist_ok=True)

    # Step 2: Install Kaggle package
    try:
        import kaggle
    except ImportError:
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle", "--quiet"])


    # Step 3: Upload Kaggle token
    from google.colab import files
    files.upload()  # prompts user to upload kaggle.json

    # Step 4: Move token to proper location
    !mkdir -p ~/.kaggle
    !mv kaggle.json ~/.kaggle/
    !chmod 600 ~/.kaggle/kaggle.json

    # Step 5: Download competition dataset

    !kaggle competitions download -c {competition_name} -p {folder_to_save}

    # Step 6: Extract all ZIP files

    # Extract all ZIP files
    for zip_file in folder_to_save.glob("*.zip"):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(folder_to_save)
        zip_file.unlink()  # remove zip
        
    # Step 7: Print contents
    print("Downloaded files:", list(folder_to_save.iterdir()))
