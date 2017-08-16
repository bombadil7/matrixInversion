#!/usr/bin/python
import sys
"""
This will be my long comment
This code will print formatted matrices.  The 
main purpose is to print the matrix received
as an argument from the outside, but as a test
get matrix as an argv, or print a default one
if there are no arguments
"""
testMatrix = "[11, 2.5, 3.2; 4.1, 5, 6; 7, 18, 9]"

def main():
    matrix = ''
    if len(sys.argv) == 2 :
        matrix = sys.argv[1]
        printMatrix(convertToNums(matrix))
    else:
        with open('in.dat') as f:
            matrices = f.readlines()
        matrices = [x.strip() for x in matrices]
        for matrix in matrices: 
            printMatrix(convertToNums(matrix))
        f.close()
    """
    elif len(sys.argv) == 1 :
        matrix = testMatrix
        printMatrix(convertToNums(matrix))
    """

def printMatrix(matrix):
    """ Some useful methods:
        (2.00).is_integer()
            True
         len(str(int(12.5)))
    """
    maxLen = 0
    maxWhole = 0
    for row in matrix:
        for val in row:
            newLen = len(str(val))
            newWhole = len(str(int(val)))
            # Ternary operator
            maxLen = newLen if newLen > maxLen else maxLen
            maxWhole = newWhole if newWhole > maxWhole else maxWhole 

    maxFrac = maxLen - maxWhole - 1
    if maxLen > 0:
        if maxWhole < 4 and maxFrac < 2:
            for row in matrix:
                print('|', end="")
                for val in row:
                    if val.is_integer():
                        print('{}{:^4d}{}'.format(' ', int(val), ' '), end="", flush=True)
                    else:
                        print('{}{:4.1f}{}'.format(' ', val, ' '), end="", flush=True)
                print('|')


        elif maxWhole < 4 and maxFrac < 3:
            for row in matrix:
                print('|', end="")
                for val in row:
                    if val.is_integer():
                        print('{}{:^5d}{}'.format(' ', int(val), ' '), end="", flush=True)
                    else:
                        print('{}{:05.2f}{}'.format(' ', val, ' '), end="", flush=True)
                print('|')


        elif maxWhole < 4 and maxFrac < 4:
            for row in matrix:
                print('|', end="")
                for val in row:
                    if val.is_integer():
                        print('{}{:^5d}{}'.format(' ', int(val), ' '), end="", flush=True)
                    else:
                        print('{}{:06.3f}{}'.format(' ', val, ' '), end="", flush=True)
                print('|')

        elif maxWhole < 4 and maxFrac < 6:
            for row in matrix:
                print('|', end="")
                for val in row:
                    if val.is_integer():
                        print('{}{:^5d}{}'.format(' ', int(val), ' '), end="", flush=True)
                    else:
                        print('{}{:08.5f}{}'.format(' ', val, ' '), end="", flush=True)
                print('|')

        elif maxWhole < 6 and maxFrac < 3:
            for row in matrix:
                print('|', end="")
                for val in row:
                    if val.is_integer():
                        print('{}{:^5d}{}'.format(' ', int(val), ' '), end="", flush=True)
                    else:
                        print('{}{:08.2f}{}'.format(' ', val, ' '), end="", flush=True)
                print('|')




        else: 
            for row in matrix:
                print('|', end="")
                for val in row:
                    if val.is_integer():
                        print('{}{:^8d}{}'.format(' ', int(val), ' '), end="", flush=True)
                    else:
                        print('{}{:08.5f}{}'.format(' ', val, ' '), end="", flush=True)
                print('|')
            
            


def convertToNums(mString):
    num = ''
    row = []
    matrix = []
    foundSpace = False
    for c in mString:
        if isNum(c):    
            num += c
            foundSpace = False
        elif isChar(c) and foundSpace == False:
            foundSpace = True
            row.append(float(num))
            num = ''

            if c == ';':
                matrix.append(row)
                row = []

    matrix.append(row)
#    print(matrix)
    return matrix




# should have used str.isdigit() instead
def isNum(c):
    if  c == '0' or \
        c == '1' or \
        c == '2' or \
        c == '3' or \
        c == '4' or \
        c == '5' or \
        c == '6' or \
        c == '7' or \
        c == '8' or \
        c == '9' or \
        c == '0' or \
        c == '.':
        return True
    else:
        return False

def isChar(c):
    if  c == ',' or \
        c == ' ' or \
        c == ']' or \
        c == ';':
        return True
    else:
        return False

if __name__ == '__main__':
    main()

