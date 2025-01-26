from paddleocr import PaddleOCR
from docx import Document
from fpdf import FPDF
import os

# Initialize PaddleOCR with English language
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Function to save text to a Word document
def save_to_word_with_page_breaks(image_texts, output_path):
    doc = Document()
    for idx, text in enumerate(image_texts):
        doc.add_paragraph(text)
        if idx < len(image_texts) - 1:
            doc.add_page_break()
    doc.save(output_path)

# Function to save text to a PDF with page breaks
def save_to_pdf_with_page_breaks(image_texts, output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Times", size=12)
    for text in image_texts:
        pdf.add_page()
        pdf.multi_cell(0, 10, text)
    pdf.output(output_path)

# Function to process an image and extract all text

def process_image(image_path):
    result = ocr.ocr(image_path, det=True)
    extracted_text = "\n".join([line[1][0] for line in result[0]])
    return extracted_text

# main function to process all images in the folder
def process_image_to_documents(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_texts = []
    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith(('.png','.jpg','.jpeg')):
            image_path = os.path.join(image_folder, image_file)
            print(f"Processing: {image_path}")
            text = process_image(image_path)
            image_texts.append(text)

    # Save all extracted texts to word and PDF with page breaks
    word_path = os.path.join(output_folder, "output.docx")
    pdf_path = os.path.join(output_folder, "output.pdf")
    save_to_word_with_page_breaks(image_texts, word_path)
    save_to_pdf_with_page_breaks(image_texts, pdf_path)
    print(f"Output saved to: {word_path}, {pdf_path}")

# Example usage
if __name__ == "__main__":
    image_folder = r"C:\Users\Rahul\Desktop\img"
    output_folder = r"C:\Users\Rahul\Desktop\output"
    process_image_to_documents(image_folder, output_folder)

















