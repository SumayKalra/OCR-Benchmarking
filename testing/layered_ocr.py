#GET text Document makes it easy to setup any of these 4 OCRs incase one fails
#COULD also 
import easyocr
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from PIL import Image
import pytesseract
from paddleocr import PaddleOCR

def get_text_Doctr(image_path):
    doc = DocumentFile.from_images(image_path)  
    model = ocr_predictor(pretrained=True)
    result = model(doc)
    print(result)

def get_text_EasyOCR(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    print(result)

def get_text_Paddle(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    result = ocr.ocr(image_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            print(line)

def get_text_Tesseract(image_path):
    image = Image.open(image_path)
    result = pytesseract.image_to_string(image, lang='eng')
    print(result)






image_path = "images/printedtext.png"
get_text_Doctr(image_path)
get_text_EasyOCR(image_path)
get_text_Paddle(image_path)
get_text_Tesseract(image_path)
