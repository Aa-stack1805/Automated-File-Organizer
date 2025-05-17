import os
import shutil
import argparse

# Mapping of extensions to folder names (optional customization)
DEFAULT_MAPPING = {
    'pdf': 'PDFs',
    'doc': 'Word Documents',
    'docx': 'Word Documents',
    'txt': 'Text Files',
    'xlsx': 'Excel Files',
    'xls': 'Excel Files',
    'pptx': 'PowerPoint Presentations',
    'ppt': 'PowerPoint Presentations',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'mp3': 'Audio',
    'wav': 'Audio',
    'mp4': 'Videos',
    'mkv': 'Videos',
    'zip': 'Archives',
    'rar': 'Archives'
}

UNKNOWN_FOLDER = 'Others'


def organize_directory(root_dir, mapping=None):
    """
    Organize files in the given directory (and its subdirectories) into folders based on file extension.

    :param root_dir: The directory to organize
    :param mapping: Optional dict mapping file extensions to folder names
    """
    if mapping is None:
        mapping = DEFAULT_MAPPING

    # Walk through directory structure
    for current_root, dirs, files in os.walk(root_dir):
        # Skip our own created folders to avoid infinite loops
        if os.path.basename(current_root) in set(mapping.values()) | {UNKNOWN_FOLDER}:
            continue

        for file in files:
            filepath = os.path.join(current_root, file)
            ext = file.lower().split('.')[-1] if '.' in file else ''
            folder_name = mapping.get(ext, UNKNOWN_FOLDER)
            target_folder = os.path.join(root_dir, folder_name)

            # Create folder if it doesn't exist
            os.makedirs(target_folder, exist_ok=True)

            # Move file to target
            try:
                shutil.move(filepath, os.path.join(target_folder, file))
                print(f"Moved: {filepath} -> {target_folder}")
            except Exception as e:
                print(f"Failed to move {filepath}: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Organize files in a directory by extension.')
    parser.add_argument('path', nargs='?', default=os.path.join(os.path.expanduser('~'), 'Downloads'),
                        help='Path to the directory to organize. Defaults to your Desktop.')
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a valid directory.")
        exit(1)

    organize_directory(args.path)
