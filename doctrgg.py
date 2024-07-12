from doctr.models import ocr_predictor
from doctr.io import DocumentFile

# Load the OCR predictor model
try:
    model = ocr_predictor(pretrained=True)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", e)

# Load your document (image or PDF)
try:
    doc = DocumentFile.from_images("printedtext.png")  # Use the correct path to your image file
    print("Document loaded successfully.")
except Exception as e:
    print("Error loading document:", e)

# Perform OCR
try:
    result = model(doc)
    print("OCR performed successfully.")
    print(result)
except Exception as e:
    print("Error during OCR:", e)
