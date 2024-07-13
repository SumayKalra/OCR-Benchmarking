import easyocr
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from PIL import Image
import pytesseract
from paddleocr import PaddleOCR
import json
import os
import logging
from difflib import SequenceMatcher
import warnings

#getting ridding of terminal dumps
warnings.filterwarnings("ignore")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
logging.getLogger("ppocr").setLevel(logging.ERROR)

def get_text_Doctr(image_path):
    doc = DocumentFile.from_images(image_path)  
    model = ocr_predictor(pretrained=True)
    result = model(doc)
    result_text = []
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                for word in line.words:
                    result_text.append(word.value)
    return {"Doctr": " ".join(result_text)}

def get_text_EasyOCR(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    result_text = [text for (_, text, _) in result]
    return {"EasyOCR": " ".join(result_text)}

def get_text_Paddle(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    result = ocr.ocr(image_path, cls=True)
    result_text = []
    for res in result:
        for line in res:
            result_text.append(line[-1][0])
    return {"PaddleOCR": " ".join(result_text)}

def get_text_Tesseract(image_path):
    image = Image.open(image_path)
    result = pytesseract.image_to_string(image, lang='eng')
    cleaned_result = result.replace('\n', ' ').strip()
    return {"Tesseract": cleaned_result}

def calculate_accuracy(ocr_result, correct_text):
    matcher = SequenceMatcher(None, ocr_result, correct_text)
    accuracy = matcher.ratio()
    return accuracy

correct_strings = [
    "This is a lot of 12 point text to test the ocr code and see if it works on all types of file format..  The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox. The quick brown dog jumped over the lazy fox.",
    "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
    "Adobe, the Adobe logo, Acrobat, the Acrobat logo, Acrobat Capture, Adobe Garamond, Adobe Intelligent Document Platform, Adobe PDF, Adobe Reader, Adobe Solutions Network, Aldus, Dis- tiller, ePaper, Extreme, FrameMaker, Illustrator, InDesign, Minion, Myriad, PageMaker, Photo- shop, Poetica, PostScript, and XMP are either registered trademarks or trademarks of Adobe Systems Incorporated in the United States and/or other countries. Microsoft and Windows are either registered trademarks or trademarks of Microsoft Corporation in the United States and/or other countries. Apple, Mac, Macintosh, and Power Macintosh are trademarks of Apple Computer, Inc., registered in the United States and other countries. IBM is a registered trademark of IBM Corporation in the United States. Sun is a trademark or registered trademark of Sun Microsys- tems, Inc. in the United States and other countries. UNIX is a registered trademark of The Open Group. SVG is a trademark of the World Wide Web Consortium; marks of the W3C are registered and held by its host institutions MIT, INRIA and Keio. Helvetica and Times are registered trade- marks of Linotype-Hell AG and/or its subsidiaries. Arial and Times New Roman are trademarks of The Monotype Corporation registered in the U.S. Patent and Trademark Office and may be regis- tered in certain other jurisdictions. ITC Zapf Dingbats is a registered trademark of International Typeface Corporation. Ryumin Light is a trademark of Morisawa & Co., Ltd. All other trademarks are the property of their respective owners.",
    "When an image is seen for only 13 milliseconds before the next image appears, a part of the brain continues to process the images longer than the amount of time it was seen.",
    "This is the first line of this text example. This is the second line of the same text.",
    "orP hseMtxeT a si sihT tresni esaelP .tcejbo .ereh txet nwo ruoy",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"

    ]

image_folder = "images"
image_files = sorted([f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))])
print(image_files)
assert len(image_files) == len(correct_strings), "Number of images and correct strings must match."

for num, (image_file, correct_text) in enumerate(zip(image_files, correct_strings)):
    image_path = os.path.join(image_folder, image_file)
    results = {}
    results.update(get_text_Doctr(image_path))
    results.update(get_text_EasyOCR(image_path))
    results.update(get_text_Paddle(image_path))
    results.update(get_text_Tesseract(image_path))

    accuracy_scores = {
        ocr_engine: calculate_accuracy(text, correct_text)
        for ocr_engine, text in results.items()
    }

    results['Accuracy'] = accuracy_scores
    results['CorrectText'] = correct_text
    print(correct_text, accuracy_scores)
    results_json = json.dumps(results, indent=4)

    output_dir = "json_files"
    os.makedirs(output_dir, exist_ok=True)

    output_file_path = os.path.join(output_dir, f"results{num+1} {image_file}.json")

    with open(output_file_path, 'w') as output_file:
        output_file.write(results_json)



