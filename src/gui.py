import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_converter import PDFConverter, convert_to_pdf

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text and Image to PDF Converter")
        self.files = []

        # GUI Elements
        self.label = tk.Label(self.root, text="Select files to convert (Text or Images):")
        self.label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Files", command=self.add_files)
        self.add_button.pack(pady=5)

        self.convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_files)
        self.convert_button.pack(pady=5)

    def add_files(self):
        filetypes = [("Text files", "*.txt"), ("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")]
        selected_files = filedialog.askopenfilenames(title="Select Files", filetypes=filetypes)
        if selected_files:
            self.files.extend(selected_files)
            messagebox.showinfo("Files Added", f"{len(selected_files)} files added successfully!")

    def convert_files(self):
        if not self.files:
            messagebox.showwarning("No Files", "Please add files to convert.")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            try:
                convert_to_pdf(self.files, output_file)
                messagebox.showinfo("Success", f"PDF created successfully at {output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()