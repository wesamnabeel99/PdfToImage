from pdfCropMargins import crop

import fitz  # PyMuPDF library
from PIL import Image
import numpy as np


def extract_images_from_pdf(pdf_file, output_dir):
    pdf_document = fitz.open(pdf_file)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        image = page.get_pixmap(matrix=fitz.Matrix(1, 1), dpi=300, alpha=True)
        image.save(f"{output_dir}/page{page_number + 1}.png")

    pdf_document.close()


def overlay_images(foreground_path, output_path):
    foreground = Image.open(foreground_path)

    gradient = np.linspace((200, 200, 200), (100, 100, 100), 900)[np.newaxis, :, :]
    background = Image.fromarray(np.uint8(gradient), 'RGB')

    background = background.resize(foreground.size, Image.ADAPTIVE)

    merged_image = Image.alpha_composite(background.convert('RGBA'), foreground.convert('RGBA'))

    merged_image.save(output_path, format='PNG')


crop(["-o", "meow_output.pdf", "-p", "0", "-a", "-5", "textdocx.pdf"])

pdf_file = 'meow_output.pdf'
output_dir = 'output_images'

overlay_images("output_images/page1.png", "merged.png")

extract_images_from_pdf(pdf_file, "output_images")
