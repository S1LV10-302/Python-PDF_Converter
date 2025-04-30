import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from pdf_converter import convert_to_pdf

class Application:
    def __init__(self):
        # Initialize the root window with a dark theme
        self.root = ttk.Window(themename="darkly")  # Use "darkly" theme for dark mode
        self.root.title("Text and Image to PDF Converter")
        self.root.geometry("800x600")  # Set window size to 800x600
        self.root.resizable(False, False)  # Disable resizing for a cleaner look
        self.files = []

        # Main Frame
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=BOTH, expand=True)

        # Title Label
        self.label = ttk.Label(main_frame, text="Text and Image to PDF Converter", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        # Add Files Button
        self.add_button = ttk.Button(main_frame, text="Add Files", command=self.add_files, bootstyle=PRIMARY)
        self.add_button.pack(pady=5)

        # Listbox Frame
        listbox_frame = ttk.Frame(main_frame)
        listbox_frame.pack(pady=10, fill=BOTH, expand=True)

        # Scrollbar for Listbox
        self.scrollbar = ttk.Scrollbar(listbox_frame, orient=VERTICAL)
        self.listbox = ttk.Listbox(listbox_frame, width=80, height=15, yscrollcommand=self.scrollbar.set, selectmode=MULTIPLE)
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Remove Selected File Button
        self.remove_button = ttk.Button(main_frame, text="Remove Selected File", command=self.remove_selected_file, bootstyle=DANGER)
        self.remove_button.pack(pady=5)

        # Convert to PDF Button
        self.convert_button = ttk.Button(main_frame, text="Convert to PDF", command=self.convert_files, bootstyle=SUCCESS)
        self.convert_button.pack(pady=10)

    def add_files(self):
        filetypes = [("Text files", "*.txt"), ("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")]
        selected_files = filedialog.askopenfilenames(title="Select Files", filetypes=filetypes)
        if selected_files:
            for file in selected_files:
                if file not in self.files:  # Avoid duplicate entries
                    self.files.append(file)
                    self.listbox.insert(END, file)  # Add file to the listbox
            messagebox.showinfo("Files Added", f"{len(selected_files)} files added successfully!")

    def remove_selected_file(self):
        selected_indices = self.listbox.curselection()  # Get selected indices
        if not selected_indices:
            messagebox.showwarning("No Selection", "Please select a file to remove.")
            return

        for index in reversed(selected_indices):  # Remove from the end to avoid index shifting
            self.listbox.delete(index)  # Remove from listbox
            del self.files[index]  # Remove from the files list

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