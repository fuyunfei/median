# -*- coding: utf-8 -*-
from scipy import signal
import numpy as np
import operator


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

x = np.arange(1,101).reshape(10, 10)
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


print (enlarge(x,2))

def median(M,win_size):
    if win_size%2==1:
        print("error")
    M=enlarge(M,(win_size)/2)
