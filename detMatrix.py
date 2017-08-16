from printMatrix import *

def main():
#aStr = '[1 2 3; 4 5 6; 7 8 9]'
#aStr = '[2 2 3; 0 1 6; 0 8 9]'
    aStr = '[2 2 3 4 0; 0 1 6 7 1; 0 8 9 6 0; 0 1 5 4 0; 0 1 3 7 9]'
#({2,2,3,4,0},{0,1,6,7,1},{0,8,9,6,0},{0,1,5,4,0},{0,1,3,7,9})
    a = convertToNums(aStr)

    printMatrix(a)
    print('Determinant is ', getDet(a))
    

class InvalidMatrixException(Exception):
    pass

def getMinorDet(m):
    if isValid2by2(m):
        # Compute the determinant
#print('getMinorDet() is called with')
#printMatrix(m)
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return False


def getDet(m):
    if False == isValid(m): # Needs to be implemented
        return False

    if False == isSquare(m):
        return False

    det = 0
    size = len(m[0])
#print("getDet() called with size = ", size)

    if isValid2by2(m):
        return getMinorDet(m)

    for i in range (size):
        det += (-1)**i * m[0][i] * getDet(getRem(m,i)) 
    return det
        
def getRem(m, exclude):
#print("getRem() is called with num = ", m[0][exclude])
    rows = len(m[0])
    newMatrix = []
    newRow = []
    for row in range (1,rows):
        for col in range (rows):
            if col != exclude:
                newRow.append(m[row][col])
                if len(newRow) == (rows - 1):
                    newMatrix.append(newRow)
                    newRow = []
#printMatrix(newMatrix)
    return newMatrix

def isValid2by2(m):
    # Check that it's a list of lists
    if type(m) is not list:
        return False

    # Check that it has 2 rows 
    if len(m) != 2:
        return False

    # Check that each row is a list too
    if type(m[0]) is not list or type(m[1]) is not list:
        return False

    # Check that rows have only two numbers
    if len(m[0]) != 2 or len(m[1]) != 2:
        return False

    # Check that the values are double/int, not string
    if  type(m[0][0]) is not float or \
        type(m[0][1]) is not float or \
        type(m[1][0]) is not float or \
        type(m[1][1]) is not float:
        return False
    return True



def valid2by2OrFail(m):
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
    return nRows == nCols  
        
def isValid(m):
    return True



if __name__ == '__main__':
    main()
