import pytesseract as tess
from PIL import Image

img=Image.open('pan.jpg')
txt=tess.image_to_string(img)
print(txt)