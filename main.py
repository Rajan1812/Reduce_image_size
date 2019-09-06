from PIL import Image
import os


size=(500,500)
def reducesize():
  for file in os.listdir('.'):
    if file.endswith('g'):
      i = Image.open(file)
      fname, extn = os.path.splitext(file)
      i.thumbnail(size)
      i.save('smaller/{}{}'.format(fname,extn))


if __name__== "__main__":
        reducesize()
