import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result_english = reader.readtext('english_signs.png')
result_nums = reader.readtext('numbers.jpeg')
result_mess = reader.readtext('messy.png')
result_example = reader.readtext('example.png')


print(result_example)
print(result_english)
print(result_nums)
print(result_mess)