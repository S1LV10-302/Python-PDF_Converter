def select_files(file_types):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilenames

    Tk().withdraw()  # Prevents the root window from appearing
    file_paths = askopenfilenames(filetypes=file_types)
    return list(file_paths)

def validate_file_type(file_path, valid_extensions):
    import os

    _, ext = os.path.splitext(file_path)
    return ext.lower() in valid_extensions