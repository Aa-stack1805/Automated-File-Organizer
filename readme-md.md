# File Organizer

A simple yet powerful Python utility that automatically organizes files in a directory based on their file extensions.

## Features

- Automatically sorts files into appropriate folders based on file type
- Works recursively through directories (while avoiding already organized folders)
- Handles various file types including documents, images, videos, audio files, and more
- Customizable extension-to-folder mapping
- Provides progress feedback during organization

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/file-organizer.git

# Navigate to the directory
cd file-organizer
```

## Usage

### Basic Usage

Run the script to organize your Downloads folder (default):

```bash
python file_organiser.py
```

### Specify a Different Directory

```bash
python file_organiser.py /path/to/your/directory
```

### Example

```bash
# Organize your Documents folder
python file_organiser.py ~/Documents
```

## Default Organization Structure

The script organizes files into the following folders by default:

- **PDFs**: `.pdf` files
- **Word Documents**: `.doc`, `.docx` files
- **Text Files**: `.txt` files
- **Excel Files**: `.xlsx`, `.xls` files
- **PowerPoint Presentations**: `.pptx`, `.ppt` files
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif` files
- **Audio**: `.mp3`, `.wav` files
- **Videos**: `.mp4`, `.mkv` files
- **Archives**: `.zip`, `.rar` files
- **Others**: Any file type not specified above

## Customization

You can customize the extension-to-folder mapping by modifying the `DEFAULT_MAPPING` dictionary in the script:

```python
DEFAULT_MAPPING = {
    'pdf': 'PDFs',
    'doc': 'Word Documents',
    # Add or modify mappings as needed
}
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only the Python standard library)

## License

[MIT](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
