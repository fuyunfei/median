import numpy as np
from skimage import exposure
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import misc
from scipy import ndimage


orig_image=misc.imread('pic/f.png')
temp=np.fft.fft2(orig_image)
fft_orig = np.fft.fftshift(np.fft.fft2(orig_image))

def butter2d_lp(shape, f, n=1, pxd=1):

#    pxd = float(pxd)
#    rows, cols = shape
#    x = np.linspace(-0.5, 0.5, cols) * cols / pxd
#    y = np.linspace(-0.5, 0.5, rows) * rows / pxd
#    radius = np.sqrt((x ** 2)[np.newaxis] + (y ** 2)[:, np.newaxis])
#    filt = 1 / (1.0 + (radius / f) ** (2 * n))
    rows, cols = shape
    filt=np.zeros(shape)
    if f>0:
        filt[0.5*(rows-rows*f):0.5*(rows+rows*f),0.5*(cols-cols*f):0.5*(cols+cols*f)]=1
    return filt

def butter2d_bp(shape, cutin, cutoff, n, pxd=1):
    return butter2d_lp(shape, cutoff, n, pxd) - butter2d_lp(shape, cutin, n, pxd)


fig = plt.figure()

for i in xrange(5):
    filt = butter2d_bp(orig_image.shape, i * 0.2, i * 0.2 + 0.2, 2, pxd=43)
    fft_new = fft_orig * filt
    new_image = np.real(np.fft.ifft2(np.fft.ifftshift(fft_new)))
    # new_image = exposure.equalize_hist(new_image)

    ax = fig.add_subplot(5, 2, 2*i+1) # this line adds sub-axes
    if  i==0:
        plt.title('filter')
    plt.gray()
    plt.axis('off')
    ax.imshow(filt) # this line creates the image using the pre-defined sub axes

    ax = fig.add_subplot(5, 2, 2*i + 2)
    if i == 0:
        plt.title('filted image ')
    plt.gray()
    plt.axis('off')
    plt.imshow(new_image)

fig.savefig('test.png')

plt.show()
