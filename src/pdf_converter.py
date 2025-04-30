from fpdf import FPDF
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

class PDFConverter:
    def __init__(self):
        self.elements = []

    def add_text(self, text):
        self.elements.append(('text', text))

    def add_image(self, image_path):
        self.elements.append(('image', image_path))

    def generate_pdf(self, output_path):
        pdf = FPDF()
        for element in self.elements:
            if element[0] == 'text':
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for line in element[1].split('\n'):
                    pdf.cell(0, 10, txt=line.strip(), ln=True)
            elif element[0] == 'image':
                image = Image.open(element[1])
                pdf.add_page()
                pdf.image(element[1], x=10, y=10, w=190)  # Adjust dimensions as needed
        pdf.output(output_path)

# ✅ New function added to support import like: from pdf_converter import convert_to_pdf
def convert_to_pdf(files, output_path):
    converter = PDFConverter()
    for file in files:
        if file.lower().endswith(".txt"):
            with open(file, "r", encoding="utf-8") as f:
                converter.add_text(f.read())
        elif file.lower().endswith((".jpg", ".jpeg", ".png")):
            converter.add_image(file)
    converter.generate_pdf(output_path)
