import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(pdf_filename, text):
    if not os.path.exists(pdf_filename):
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        y_position = 750
        c.drawString(100, y_position, text)
        c.save()
        print(f"PDF '{pdf_filename}' created successfully.")
    else:
        print(f"PDF '{pdf_filename}' already exists.")
