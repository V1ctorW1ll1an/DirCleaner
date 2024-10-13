import argparse
import shutil
from pathlib import Path
import logging

# Configura o logging
logging.basicConfig(
    filename="file_operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def delete_files(folder: Path) -> None:
    for file_path in folder.iterdir():
        try:
            if file_path.is_file() or file_path.is_symlink():
                file_path.unlink()
            elif file_path.is_dir():
                shutil.rmtree(file_path)
            logging.info(f"Deleted: {file_path}")
        except FileNotFoundError:
            logging.error(f"File {file_path} not found.")
        except PermissionError:
            logging.error(f"Permission denied to delete {file_path}.")
        except Exception as e:
            logging.error(f"Failed to delete {file_path}. Reason: {str(e)}")


def list_files(folder: Path) -> None:
    for file_path in folder.iterdir():
        print(file_path.name)


def main() -> None:
    parser = argparse.ArgumentParser(description="Path to your folder")
    parser.add_argument("--path", required=True, help="Path to the folder")
    parser.add_argument("--list", action="store_true", help="List files in the folder")
    args = parser.parse_args()

    FOLDER = Path(args.path)
    if not FOLDER.exists():
        print(f"The folder {FOLDER} does not exist.")
        return

    if args.list:
        list_files(FOLDER)
    else:
        confirm = input(
            f"Are you sure you want to delete all contents of {FOLDER}? (y/n): "
        )
        if confirm.lower() == "y":
            delete_files(FOLDER)
        else:
            print("Operation cancelled.")


if __name__ == "__main__":
    main()
