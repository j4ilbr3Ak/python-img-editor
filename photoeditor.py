import sys 
import os
from PIL import Image, ImageEnhance, ImageFilter


path = '/home/j4ilbr3k/Pictures/imgs'
pathOut = '/home/j4ilbr3k/Pictures/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
