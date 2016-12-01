# -*- coding: utf-8 -*-
from scipy import signal
import numpy as np
import os
import operator
from scipy import misc


#x = np.arange(100).reshape(10, 10)
#domain = np.ones((3,3))
#print(domain)
#print(x)
#medx=signal.order_filter(x, domain, 0)
#print(medx)
#medx2= signal.medfilt(x,3)
#print(medx2)


#周边取 0
#x = np.random.randint(10,size=(10,10))
#for i in range(1,2):
#	medx2= signal.medfilt(x,5)
#	x=x-medx2 
#print(x)
#print(medx2)

#x = np.random.randint(1,10,size=(5,5))
##x = np.arange(100).reshape(10, 10)
#domain = np.ones((3,3))
#medx=signal.order_filter(x, domain, 2)
#print(x)
#print(domain)
#print(medx)

# 放大 array
#def  enlarge(x,addsize):
#    for i in range(addsize):
#        #c=tuple(map(operator.add, x.shape, (1,1)))
#        a=[x[0,:]]
#        x=np.concatenate((a, x), axis=0)
#        a = [x[x.shape[0]-1, :]]
#        x = np.concatenate((x,a), axis=0)
#        a = [x[:,0]]
#        print(a.transpose())
#        print(x)
#        x = np.concatenate((a, x), axis=1)
#
#   return  x

#x = np.arange(1,101).reshape(10, 10)
#x = misc.imread('f.png')
np.random.seed(0)
x = np.random.randint(1,255,size=(10,10))
with open('test1.csv','a+') as f:
	f.write('X\n' )
	np.savetxt(f, x, fmt='%d', delimiter=",");

misc.imsave('x.png',x)
def  enlarge(x,addsize):

    for i in range(addsize):
        enlarge_x = np.zeros((x.shape[0] + 2, x.shape[1] + 2))
        enlarge_x[1:-1, 1:-1] = x
        enlarge_x[0,:]=enlarge_x[1,:]
        enlarge_x[-1,:]=enlarge_x[-2,:]
        enlarge_x[:,0] = enlarge_x[:,1]
        enlarge_x[:, -1] = enlarge_x[:, -2]
        x=enlarge_x
    return enlarge_x

def med(M,win_size):
    if win_size%2 ==1:
    	r=(win_size-1)/2
    	Med_M=np.zeros((M.shape[0]-2*r,M.shape[1]-2*r))
    for i in range(M.shape[0]-r):
    	#M=enlarge(M,r)
    	for j in range(M.shape[1]-r):
    		cur_arr=M[i-r:i+r+1,j-r:j+r+1]
    		Med_M[i-r,j-r]=np.median(cur_arr)
    return Med_M


def itermed(M,win_size,iter_num):
	r=(win_size-1)/2
	for i in xrange(1,30):
		med_M=med(enlarge(M,r),win_size)
		M=M-med_M
		misc.imsave('med%02d.png' % i, med_M)
		with open('test1.csv','a+') as f:
			f.write('Med%02d\n'%i)
			np.savetxt(f, med_M, fmt='%d', delimiter=",");
			f.write('f%02d\n'%i)
			np.savetxt(f, M,fmt='%d',delimiter=",");

	return med_M

print x
itermed(x,3,4)