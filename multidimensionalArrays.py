import numpy as np

array = np.array("A") #0 dim array
print(array.ndim)#0

array1 = np.array([1,2])
print(array1.ndim)#1

array2 = np.array([[1]])
print(array2.ndim)#2

array3 = np.array([[[1]]])
print(array3.ndim)#3
