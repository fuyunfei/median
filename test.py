import Image, ImageFilter
from numpy import array
im = Image.open('f.png')
 

for i in range(10):

	median = im.filter(ImageFilter.MedianFilter(11))
	median.save('./med/med%d.png'%i)
	arr = array(median)
	im = array(im)
	im=im-median
	im = Image.fromarray(im)
	im.save('./res/res%d.png'%i)

