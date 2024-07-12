from doctr.models import ocr_predictor
from doctr.io import DocumentFile

# Load the OCR predictor model
try:
    model = ocr_predictor(pretrained=True)
except Exception as e:
    print("Model not loading:", e)

doc = DocumentFile.from_images("printedtext.png")  


try:
    result = model(doc)
    print(result)
except Exception as e:
    print("Error in OCR:", e)
