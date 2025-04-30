<<<<<<< HEAD
# Python-PDF_Converter
=======
# PDF Converter

This project is a Python application that allows users to convert multiple selected texts and images into a PDF file. It features a graphical user interface (GUI) for easy interaction and file selection.

## Project Structure

```
pdf-converter
├── src
│   ├── main.py          # Entry point of the application
│   ├── gui.py           # Contains the GUI layout and elements
│   ├── pdf_converter.py  # Main logic for PDF conversion
│   └── utils
│       └── file_handler.py # Utility functions for file operations
├── requirements.txt     # Lists the dependencies required for the project
├── .gitignore           # Specifies files and directories to ignore by Git
└── README.md            # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pdf-converter
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Use the GUI to select the text and image files you want to convert into a PDF.

3. Click the "Convert" button to generate the PDF file.

## Dependencies

This project requires the following Python packages:

- `reportlab`: For generating PDF files.
- `tkinter`: For creating the graphical user interface.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
>>>>>>> e084987 (Initial commit)
