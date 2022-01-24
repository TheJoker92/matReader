import scipy.io
import numpy as np

class MatApi:

    """
    Given an array retrieve the number of rows
    :param array: input vector
    :return: returns the number of rows
    """
    def getNumRows(self, array):
        return array.shape[0]

    """
    Given an array retrieve the number of cols
    :param array: input vector
    :return: returns the number of cols
    """
    def getNumCols(self, array):
        cols = 1
        if len(array.shape) > 1:
            cols = array.shape[1]
        return cols

    """
    Read the mat file
    :param matFilePath: path of .mat file
    :return: returns the content of .mat file
    """
    def readMatFile(self, matFilePath):
        return scipy.io.loadmat(matFilePath)

    """
    Given vector V returns the length of the largest array dimension in V

    :param array: input vector
    :return: the greatest between rows and cols
    """ 
    def vectorLength(self, array):
        length = 1

        rows = self.getNumRows(array)
        cols = self.getNumCols(array)

        if rows > cols:
            length = rows
        else:
            length = cols

        return length

    """
    Create a 2-dimensional array of zeros

    :param rows: number of rows
    :param cols: number of cols
    :return: a numpy array of size rows x cols
    """ 
    def zeros(self, rows, cols):
        return np.zeros((rows, cols))

    """
    Retrieves dimension of multi-dimensional array

    :param array: input vector
    :return: a tuple of array dimensions
    """
    def size(self, array):
        return array.shape

    """
    Retrieves the smallest value in the multi dimensional array

    :param array: input vector
    :return: the smallest value in the multi dimensional array
    """
    def min(self, array):
        return np.amin(array)

    """
    Given two array retrieves the difference element for element

    :param array1: input vector
    :param array2: input vector
    :return: array of the differences
    """
    def array_diff(self, array1, array2):
        return np.subtract(array1, array2)

    """
    unique(array) returns the same data as in A, but with no repetitions. C is in sorted order.

    :param array: input vector
    :return: a sorted array with no repetition respect to input
    """
    def unique(self, array):
        return np.unique(array)

    """
    Create a vector of n logarithmically spaced points in the interval [10^start,10^stop].
    :param start: first value of the interval
    :param start: last value of the interval
    :param n: number of elements
    :return: a sorted array with no repetition respect to input
    """
    def logspace(self, start, stop, n=50):
        return np.logspace(start, stop, n)

    """
    S = sum(A) returns the sum of the elements of A along the first array dimension whose size does not equal 1.
    :param start: first value of the interval
    :param start: last value of the interval
    :param n: number of elements
    :return: a sorted array with no repetition respect to input
    """
    def sum(self, array):

        rows = self.getNumRows(array)
        cols = self.getNumCols(array)

        count = self.zeros(rows, cols)

        if rows > 1:
            count = np.sum(array[0], axis=0)
        elif cols > 1:
            count = np.sum(array, axis=1)


        return count   


    """
    Find indices and values of nonzero elements.
    :param posmax: first value of the interval
    :return: an array of index of non-zeros elements
    """
    def find(self, posMax):
        return np.argwhere(posMax)

    """
    Check if array is empty:
    :param array: input array
    :return: True if array contains no element
    """
    def isempty(array):
        return array.size == 0