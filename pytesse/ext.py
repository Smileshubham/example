import pytesseract as tess
from PIL import Image

img=Image.open('image_path')
txt=tess.image_to_string(img)
print(txt)
