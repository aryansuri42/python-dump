import numpy as np
from PIL import Image
data = np.zeros((5,4,3), dtype=np.uint8)
data[:]=[69,45,0]
print(data)

data[1:4,1:3] = [0,69,0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')