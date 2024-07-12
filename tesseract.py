from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

# Load the image from the file path
image_path = "/Users/sumay.kalra/ocr_benchmarking/printedtext.png"  # Replace with your file path
image = Image.open(image_path)



# Save the processed image for debugging
processed_image_path = "/Users/sumay.kalra/ocr_benchmarking/printedtext.png"
image.save(processed_image_path)

# Display the processed image to verify preprocessing

# Perform OCR on the processed image
text = pytesseract.image_to_string(image, lang='eng')

# Print the recognized text
print(f"Extracted Text: {text}")

# Check if the processed image is saved correctly
print(f"Processed image saved at: {processed_image_path}")
