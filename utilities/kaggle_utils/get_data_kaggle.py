def get_data_kaggle_competition(folder_to_save, competition_name):
    """
    Download and extract a Kaggle competition dataset in Google Colab.
    
    Parameters
    ----------
    folder_to_save : str or pathlib.Path
        Folder where the dataset will be saved.
    competition_name : str
        Exact name of the Kaggle competition (e.g., "eliva-25-medical").
    """
    from pathlib import Path
    import zipfile
    import os
    import subprocess
    import sys
    from google.colab import files

    folder_to_save = Path(folder_to_save)
    folder_to_save.mkdir(parents=True, exist_ok=True)

    # Install Kaggle if missing
    try:
        import kaggle
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "kaggle", "--quiet"])
        import kaggle

    # Always ask for kaggle.json to avoid path issues
    print("[INFO] Please upload your kaggle.json token.")
    files.upload()
    kaggle_path = Path.home() / ".kaggle/kaggle.json"
    os.makedirs(kaggle_path.parent, exist_ok=True)
    os.rename("kaggle.json", kaggle_path)
    os.chmod(kaggle_path, 0o600)

    # Download dataset
    subprocess.check_call([
        sys.executable, "-m", "kaggle", "competitions", "download",
        "-c", competition_name,
        "-p", str(folder_to_save)
    ])

    # Extract all ZIP files
    for zip_file in folder_to_save.glob("*.zip"):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(folder_to_save)
        zip_file.unlink()  # remove zip

    print("Downloaded files:", list(folder_to_save.iterdir()))


