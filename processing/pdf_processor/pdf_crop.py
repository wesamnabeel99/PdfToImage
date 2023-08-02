from pdfCropMargins import crop
import fitz

def crop_pdf(input_path,output_path):
    crop(["-o", f"{output_path}", "-p", "0", "-a", "-5", f"{input_path}"])


def extract_images_from_pdf(pdf_file, output_dir):
    pdf_document = fitz.open(pdf_file)

    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        image = page.get_pixmap(matrix=fitz.Matrix(1, 1), dpi=300, alpha=True)
        image.save(f"{output_dir}/page{page_number + 1}.png")

    pdf_document.close()



