from pdfCropMargins import crop
from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert the PDF to a list of PIL images
    images = convert_from_path(pdf_path,dpi=300)

    # Save each image to the output folder
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f'page_{i}.png'), 'PNG')



crop(["-o","meow_output.pdf","-p","0","-a","-5", "test.pdf"])

pdf_file = 'meow_output.pdf'
output_dir = 'output_images'

pdf_to_images(pdf_path=pdf_file,output_folder="output_images")