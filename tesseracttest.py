import cv2
import pytesseract


def extract_text_from_image(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use OCR to extract text
    text = pytesseract.image_to_string(gray)

    return text.strip()

print(extract_text_from_image("./cropped_screenshot.png"))
