import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('./cropped_screenshot.png')

print(result)
result_text = ""

for (bbox, text, prob) in result:
    print(f'{text} ({prob:.1f})')
    result_text+= text + " "

print(result_text)

