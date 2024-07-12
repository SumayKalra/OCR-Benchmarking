import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result_english = reader.readtext('images/english_signs.png')
result_nums = reader.readtext('images/numbers.jpeg')
result_mess = reader.readtext('images/messy.png')
result_example = reader.readtext('images/example.png')


print(result_example)
print(result_english)
print(result_nums)
print(result_mess)