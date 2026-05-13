import easyocr

# Load EasyOCR model
reader = easyocr.Reader(['en'])

def recognize_text(processed_image):

    # Detect text
    results = reader.readtext(processed_image)

    text = ""

    # Extract detected text
    for result in results:
        text += result[1] + " "

    # Handle empty output
    if text.strip() == "":
        return "No text detected"

    return text