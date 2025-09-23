from pathlib import Path
import zipfile
import os
import subprocess
import shutil

def download_kaggle_competition(slug, dest_path="/content/kaggle_data"):
    """
    Download and extract a Kaggle competition dataset.
    
    Assumes kaggle.json is already configured in ~/.kaggle/
    
    slug: str -> Kaggle competition name
    dest_path: str -> folder where the dataset will be saved
    """
    dest_path = Path(dest_path)
    
    # Check if folder exists
    if dest_path.is_dir():
        # If folder exists but is empty, remove and recreate
        if not any(dest_path.iterdir()):
            print(f"{dest_path} exists but is empty, recreating...")
            shutil.rmtree(dest_path)
            dest_path.mkdir(parents=True, exist_ok=True)
        else:
            print(f"{dest_path} directory exists and is not empty.")
    else:
        # If folder does not exist, create it
        print(f"Did not find {dest_path} directory, creating...")
        dest_path.mkdir(parents=True, exist_ok=True)
    
    # Install Kaggle API if not already installed
    try:
        import kaggle
    except ImportError:
        print("Installing Kaggle API...")
        os.system("pip install kaggle --quiet")
    
    # Download the competition dataset
    print(f"Downloading competition '{slug}' to {dest_path} ...")
    subprocess.run(f"kaggle competitions download -c {slug} -p {dest_path}", shell=True, check=True)
    
    # Extract all zip files in the destination folder
    for zip_file in dest_path.glob("*.zip"):
        print(f"Extracting {zip_file} ...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(dest_path)
    
    # Print the final list of files
    print("Done! Files in destination:", list(dest_path.iterdir()))
