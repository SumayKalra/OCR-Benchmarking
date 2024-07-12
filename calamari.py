from calamari_ocr.ocr.predictor import Predictor
from calamari_ocr.ocr import MultiModel
import numpy as np
from PIL import Image
import re

# Function to filter out text with numbers
def filter_text(ocr_results):
    filtered_text = []
    for result in ocr_results:
        for prediction in result.outputs:
            text = prediction.sentence
            # Check if the text contains any numbers
            if not any(char.isdigit() for char in text):
                filtered_text.append(text)
    return filtered_text

# Load your document (image)
image_path = "english_signs.png"  # Replace with your file path
image = Image.open(image_path).convert('L')  # Convert to grayscale

# Convert image to numpy array
image_array = np.array(image)

# Load the pre-trained model
model_path = '/Users/sumay.kalra/Downloads/calamari_models-2.0/uw3-modern-english'  # Replace with your downloaded model path
multi_model = MultiModel([model_path])

# Create a predictor
predictor = Predictor(multi_model)

# Perform OCR
ocr_results = predictor.predict_raw([image_array])

# Get the filtered text
filtered_text = filter_text(ocr_results)

# Print the filtered text
for text in filtered_text:
    print(text)
