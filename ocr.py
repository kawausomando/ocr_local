import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import sys

def extract_text_from_pdf(pdf_file_path):
    doc = fitz.open(pdf_file_path)

    # 各ページからテキストを抽出
    extracted_text = ""
    for page in doc:
        # ページから画像を取得
        pix = page.get_pixmap()
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # pytesseractを使用してOCRを実行
        # 縦書きの場合は、lang="jpn_vert"を指定する
        text = pytesseract.image_to_string(image, lang="jpn")
        extracted_text += text + "\n"

    doc.close()
    
    return extracted_text

if __name__ == "__main__":
    pdf_file_path = sys.argv[1]
    text = extract_text_from_pdf(pdf_file_path)
    print(text)
