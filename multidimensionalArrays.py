import numpy as np
array = np.array("A") # 0 dimension array
array1 = np.array(["A", "B", "C"]) #1 dimension array, a single row

array2 = np.array([["A", "B", "C"],
                    ["A", "B", "C"]]) #2 dimension array, a single row

array3 = np.array([[["A"]]])
print(array.ndim) #number of dimension of the numpy array

print(array2.ndim)
print(array3.ndim)

#array1 = np.array("A") 
