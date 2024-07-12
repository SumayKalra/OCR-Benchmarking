from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')
img_path = 'printedtext.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)
