from PIL import Image
import pytesseract

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    text = extract_text('product_image.jpg')
    print(text)

