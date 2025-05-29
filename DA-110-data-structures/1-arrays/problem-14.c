/*
14. Write a program in C to calculate the determinant of a 3 x 3 matrix.

Test Data :

Input elements in the first matrix :

element - [0],[0] : 1

element - [0],[1] : 0

element - [0],[2] : -1

element - [1],[0] : 0

element - [1],[1] : 0

element - [1],[2] : 1

element - [2],[0] : -1

element - [2],[1] : -1

element - [2],[2] : 0

Expected Output :

The matrix is :

1 0 -1

0 0 1

-1 -1 0

The Determinant of the matrix is: 1
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