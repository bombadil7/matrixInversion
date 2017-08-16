from printMatrix import *

def main():
    aStr = '[1 2; 1 2]'
    a = convertToNums(aStr)

    print('determinant of ');
    printMatrix(a)
    res = getMinorDet(a)
    print(' = ', res)
#    print(' = {:f}'.format(res))

    if isSquare(a):
        print("The matrix is square")
    else:
        print("The matrix is not square")
    

class InvalidMatrixException(Exception):
    pass

def getMinorDet(m):
    # Compute the determinant
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]



def getDet(m):
    if isSquare(m) and isValid2by2(m):
        return getMinorDet(m)
    
        

def isValid2by2(m):
    # Check that it's a list of lists
    if type(m) is not list:
        raise InvalidMatrixException('Argument is not in correct matrix format (list)')

    # Check that it's 2 by 2
    if len(m) != 2:
        raise InvalidMatrixException('More than two rows in the matrix')

    # Check that each row is a list too
    if type(m[0]) is not list or type(m[1]) is not list:
        raise InvalidMatrixException('Wrong matrix format.  Rows of the matrix are not lists')

    # Check that rows have only two numbers
    if len(m[0]) != 2 or len(m[1]) != 2:
        raise InvalidMatrixException('Matrix is not symmetric. Rows are not two items long')

    # Check that the values are double/int, not string
    if  type(m[0][0]) is not float or \
        type(m[0][1]) is not float or \
        type(m[1][0]) is not float or \
        type(m[1][1]) is not float:
        raise InvalidMatrixException('Numbers in the matrix are not floats')



#def is2by2(m):



def isSquare(m):
    # Check that it's a list of lists
    if type(m) is not list:
        raise InvalidMatrixException('Argument is not in correct matrix format (list)')
    nRows = len(m)
    nCols = 0

    for n in range (nRows):
        # Check that each row is a list too
        if type(m[n]) is not list:
            raise InvalidMatrixException('Wrong matrix format.  Rows of the matrix are not lists')
        
        if n == 0:
            nCols = len(m[n])
        elif len(m[n]) != nCols:
           return False 
    return True
        




if __name__ == '__main__':
    main()
