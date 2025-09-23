def get_data_kaggle_competition(folder_to_save, competition_name, kaggle_json_path):
    """
    Download and extract a Kaggle competition dataset in Python.
    Deletes the zip file after extraction to save space.

    Parameters
    ----------
    folder_to_save : str or pathlib.Path
        Folder where the dataset will be saved.
    competition_name : str
        Exact name of the Kaggle competition.
    kaggle_json_path: str
        Path to the personal kaggle.json file.
    """
    from pathlib import Path
    import zipfile
    import kaggle
    import os
    import shutil

    # Asegurarse de que folder_to_save es un Path
    folder_to_save = Path(folder_to_save)
    
    # Crear la carpeta si no existe
    if folder_to_save.is_dir():
        print(f"{folder_to_save} directory exists.")
    else:
        print(f"Did not find {folder_to_save} directory, creating...")
        folder_to_save.mkdir(parents=True, exist_ok=True)

    # Configurar kaggle.json dinámicamente
    kaggle_dir = Path("/root/.kaggle")
    kaggle_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(kaggle_json_path, kaggle_dir / "kaggle.json")
    os.chmod(kaggle_dir / "kaggle.json", 0o600)
    print(f"kaggle.json configured at {kaggle_dir / 'kaggle.json'}")

    # Descargar datos de la competición
    print(f"Downloading {competition_name} into {folder_to_save}...")
    kaggle.api.competition_download_files(competition_name, path=str(folder_to_save))

    # Construir ruta del archivo zip
    zip_file = folder_to_save / f"{competition_name}.zip"

    # Descomprimir y eliminar zip
    if zip_file.exists():
        print(f"Extracting {zip_file}...")
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(folder_to_save)
        print("Extraction complete.")

        # Eliminar zip
        os.remove(zip_file)
        print(f"Deleted zip file {zip_file} to save space.")
    else:
        print(f"Error: {zip_file} not found. Check if download was successful.")

    # Listar archivos descargados
    print("Downloaded and extracted files:", list(folder_to_save.iterdir()))
