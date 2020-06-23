__author__ = 'VARSHA'

import numpy as np

def fun(arrlist):
    for i in arrlist:
        if(isinstance(i,list)):
            fun(i)
        else:
            newarr.append(i)
    return newarr
arr = np.array([1,2,[8,9],3,4,[5,[10,21,[5]],6,7]],dtype=object)
arr_iterator = arr.flat
arrlist = list(arr_iterator)
newarr=[]
print(fun(arrlist))