/*
15. Write a program in C to accept a matrix and determine whether it is a sparse matrix.

Test Data :

Input the number of rows of the matrix : 2

Input the number of columns of the matrix : 2

Input elements in the first matrix :

element - [0],[0] : 0

element - [0],[1] : 0

element - [1],[0] : 1

element - [1],[1] : 0

Expected Output :

The given matrix is sparse matrix.

There are 3 number of zeros in the matrix
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A[3][3]; // 2D array
    int size = 3 * 3;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("\nelement - [%d][%d] : ", i, j);
            scanf("%d", &A[i][j]);
        }
    }

    // print
    printf("\n\nThe matrix is:\n");
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%d  ", A[i][j]);
        }
        printf("\n");
    }

    return 0;
}