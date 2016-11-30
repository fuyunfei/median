from scipy import misc
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

# from PIL import Image

# from resizeimage import resizeimage

#   with Image.open(f) as image:
#        cover = resizeimage.resize_cover(image, [100, 100])
#       cover.save('face1.png', image.format)

# f = misc.face(gray=True)
# misc.imsave('face.png', f)
# plt.imshow(f, cmap=plt.cm.gray)

f = misc.imread('face1.png')

for i in range(1,1000):

    m = ndimage.median_filter(f, 2)

    f=f-m

plt.imshow(f, cmap=plt.cm.gray)
plt.show()
