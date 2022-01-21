import scipy.io
import numpy as np

class MatApi:

    def readMatFile(self, matFilePath):
        return scipy.io.loadmat(matFilePath)

    """
    Given vector V returns the length of the largest array dimension in V

    :param array: input vector
    :return: the greatest between rows and cols
    """ 
    def vectorLength(self, array):
        length = 0
        rows = len(array[0])
        cols = len(array)

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



matApi = MatApi()

# readfile
mat = matApi.readMatFile("V.mat")


select = 4
display = 1

V = matApi.array_diff(mat["V"], matApi.min(mat["V"]))


n = matApi.vectorLength(mat["V"])

#definition of local variables
buffer = matApi.zeros(n,1)
criterion = matApi.zeros(n,1)
if select < 1:
    minDist = n/20
else:
    minDist = n/select

#horizons = round(linspace(1,ceil(n/20),50));
horizons = matApi.unique(np.round(matApi.logspace(0,2,50)/100*np.ceil(n/20)))
#horizons=1:2:50;
Vorig = V
#all this tempMat stuff is to avoid calling findpeaks which is horribly
# slow for our purpose
tempMat = matApi.zeros(n,3)
tempMat[1][1]=float("inf")
tempMat[-1][2]=float("inf")
print(matApi.array_diff(mat["V"], matApi.min(mat["V"])))


