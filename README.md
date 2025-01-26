# OCR Text Extractor with PaddleOCR

## Overview
This project automates the process of extracting text from images and exporting the text to both Word and PDF documents. It uses PaddleOCR for high-accuracy optical character recognition (OCR), ensuring reliable text detection and extraction.

Each image's text is saved on a separate page in the Word and PDF files, making the documents well-structured and easy to read.

---

## Features
- Extracts text from images (supports PNG, JPG, JPEG formats).
- Saves the extracted text to a Word document with page breaks between each image's text.
- Creates a PDF file with page breaks for text from each image.
- High accuracy using PaddleOCR.

---

## Requirements
### Python Dependencies:
- `paddleocr`
- `paddlepaddle`
- `python-docx`
- `fpdf`

### Installation
Run the following command to install all dependencies:

```bash
pip install paddleocr paddlepaddle python-docx fpdf
```

---

## Project Structure
```
project_folder/
├── images/                  # Folder containing the input images
├── output/                  # Folder where Word and PDF files will be saved
├── main.py                  # Main script to run the project
├── README.md                # Project documentation
└── requirements.txt         # List of dependencies
```

---

## Usage

### 1. Prepare Input Images
Place all the images you want to process into a folder (e.g., `C:\Users\Rahul\Desktop\img`).

### 2. Run the Script
Run the `main.py` script using the following command:

```bash
python main.py
```

### 3. Outputs
The script will generate two output files:
- `output.docx`: A Word document with each image's text on a separate page.
- `output.pdf`: A PDF file with each image's text on a separate page.

These files will be saved in the specified output folder (e.g., `C:\Users\Rahul\Desktop\output`).

---

## Example Code
Below is the core Python code to run the project:

```python
from paddleocr import PaddleOCR
from docx import Document
from fpdf import FPDF
import os

# Initialize PaddleOCR with English language
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Function to save text to a Word document with page breaks
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

# Main function to process all images in the folder
def process_images_to_documents(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_texts = []
    for image_file in os.listdir(image_folder):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, image_file)
            print(f"Processing: {image_path}")
            text = process_image(image_path)
            image_texts.append(text)

    # Save all extracted texts to Word and PDF with page breaks
    word_path = os.path.join(output_folder, "output.docx")
    pdf_path = os.path.join(output_folder, "output.pdf")
    save_to_word_with_page_breaks(image_texts, word_path)
    save_to_pdf_with_page_breaks(image_texts, pdf_path)
    print(f"Output saved to: {word_path}, {pdf_path}")

# Example usage
if __name__ == "__main__":
    image_folder = r"C:\Users\Rahul\Desktop\img"
    output_folder = r"C:\Users\Rahul\Desktop\output"
    process_images_to_documents(image_folder, output_folder)
```

---

## Notes
1. Ensure PaddleOCR dependencies are installed properly before running the script.
2. If you encounter any issues, verify that your Python version is compatible with the libraries (recommended: Python 3.7+).

---

## License
This project is open-source and free to use under the [MIT License](LICENSE).

---

## Contributing
If you have suggestions or would like to enhance this project, feel free to submit a pull request or raise an issue.

---