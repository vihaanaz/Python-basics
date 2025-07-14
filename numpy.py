import numpy
import numpy as np
arr = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

print(np.__version__)

arr = np.array(42)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr = np.array(42)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

arr = np.array([1, 2, 3, 4], ndmin=5) 
print(arr) 
print('number of dimensions :', arr.ndim)

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) 
