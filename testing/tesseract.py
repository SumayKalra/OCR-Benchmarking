from PIL import Image
import pytesseract

image_path = "/Users/sumay.kalra/ocr_benchmarking/images/printedtext.png"  
image = Image.open(image_path)
text = pytesseract.image_to_string(image, lang='eng')
print(f"Extracted Text: {text}")

