#Matrix Multiplication of any order
A_Row = int(input("Enter the rows of first Matrix:"))
A_Col = int(input("Enter the Columns of first Matrix:"))

B_Row = int(input("Enter the rows of second Matrix:"))
B_Col = int(input("Enter the Columns of second Matrix:"))

# Take three matrix
matrixA = []
matrixB = []
result = []

#define find element at i, j position and return the value
def calElement(i,j,order):
    sum = 0
    for k in range(order):
        sum += matrixA[i][k]*matrixB[k][j]
    return sum
#TODO: define function to take matrix input
def inputMatrix(row,column,matrix):
    for i in range(row):
        a = []
        for j in range(A_Col):
            a.append(int(input()))
        matrix.append(a)

if(A_Col != B_Row):
    print("Multiplication can not be performed\nColumns of first and Row of second Matrix does not match")
else:
    # Take input in Matrix first Matrix
    print("Enter the elements of first matrix")
    inputMatrix(A_Row,A_Col,matrixA)
    # Take input in Matrix second Matrix
    print("Enter the elements of second matrix")
    inputMatrix(B_Row,B_Col,matrixB)

    #Multiply both matrix
    print("Please Wait....")
    for i in range(A_Row):
        a = []
        for j in range(B_Col):
            a.append(calElement(i,j,max(A_Row,B_Col)))
        result.append(a)
    print("The result is")
    print(result)
