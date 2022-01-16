
from PIL import Image

babler = 1
while True:
  image = Image.open(f'bablerjpg/babler ({babler}).jpg')
  image.save(f'bablerpng/babler{babler}.png')
  babler += 1
  if babler == 74:
    break
