##### ----- imports ----- #####
import numpy as np

##### ----- Variables ----- #####
arr0 = np.array(['banana', 'cherry', 'apple'])
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr5 = np.array([6,5,4,3,2,1])
arr0d = np.array(42)
arr1d = np.array([1,2,3,4,5,6])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr5d = np.array([1,2,3,4], ndmin=5)

##### ----- Functions ----- #####
def fun_copy():
    arr = np.array([1,2,3,4,5])
    x = arr.copy()
    arr[0] = 42
    print('copy not effected:')
    print('(original, copy) : ', (arr, x))

def fun_view():
    arr = np.array([1,2,3,4,5])
    x = arr.view()
    arr[0] = 42
    print('copy is effected:')
    print('(original, copy) : ', (arr, x))

def filter():
    a1 = np.array([41, 42, 43, 44])
    filter = a1 % 2 == 0
    print('filter - index filter: ', filter)
    print('filter - apply filter: ', a1[filter])


##### ----- Calls ----- #####
#Dimension in Arrays
print(' -- Dimension in Arrays --')
print(arr0d.ndim, arr1d.ndim, arr2d.ndim, arr3d.ndim)
print('number of dimensions : ', arr5d.ndim, arr5d, )
print('shape: ', arr1d.shape, arr2d.shape, arr3d.shape, arr5d.shape, '\n\n')

#Access Array Elements
print(' -- Access Array Elements --')
print('2nd element on 1st row: ', arr2d[0, 1])
print('3rd element of the 2nd array of the 1st array: ', arr3d[0, 1, 2])
print('arrays can also be accessed from the end: ', arr1d[-2])
print('positive slicing : ', arr1d[2:4])
print('negative slicing : ', arr1d[-4:-2])
print('step slicing (every other element): ', arr1d[0:3:2])
print('step slicing (every other element): ', arr1d[::2])
print('from both elements, return index 2: ', arr2d[0:2, 2], '\n\n')

#Fun / view
print(' -- Fun / view --')
fun_copy()
fun_view()
print('\n\n')

#Joining arrays
print(' -- Joining arrays --')
print('concat: ', np.concatenate((arr1, arr2)))
print('concat axis = 0:\n', np.concatenate((arr3, arr4), axis=0))
print('concat axis = 1:\n', np.concatenate((arr3, arr4), axis=1))
print('vstack:\n', np.vstack((arr1, arr2)))
print('hstack:\n', np.hstack((arr1, arr2)))
print('dstack:\n', np.dstack((arr1, arr2)))
print('split:\n', np.array_split(arr1d, 3), '\n\n')

#Search / Sort arrays
print(' -- Search / Sort arrays --')
print('search - where: ', np.where(arr1d%2 == 0))
print('search - Binary search: ', np.searchsorted(arr1d, 4))
print('sort - alphabetically: ', np.sort(arr0))
print('sort - mergesort: ', np.sort(arr5, kind='mergesort'))
filter()