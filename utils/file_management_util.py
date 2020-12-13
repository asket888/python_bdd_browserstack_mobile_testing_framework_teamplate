from pathlib import Path


def get_absolute_path_to_folder(folder_name: str) -> str:
    """
    Return absolute path to chosen folder in main directory
    :return: absolute path as string string
    """
    return str(Path(Path(__file__).parent.parent, folder_name))
