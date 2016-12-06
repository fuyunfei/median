import numpy as np
import theano
import theano.tensor as T
from theano.tensor import fft
import theano.sandbox.fourier as tsf
import Image, ImageFilter
import matplotlib.pyplot as plt
im = Image.open('./pic/f.png')


x = T.matrix('x', dtype='float64')


rfft = fft.rfft(x)
y=rfft.type()
ifft = fft.irfft(y)
f_rfft = theano.function([x],rfft)
f_ifft = theano.function([y],ifft)


out = f_rfft(im)
rec=f_ifft(out)
plt.imshow(out[:,:,0], 'gray')

plt.imshow(rec, 'gray')
plt.show()
#c_out = np.asarray(out[0, :, 0] + 1j*out[0, :, 1])
#abs_out = abs(c_out)

