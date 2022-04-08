import numpy
def determinant(matrix):
    a = numpy.array(matrix)
    return round(numpy.linalg.det(a))

