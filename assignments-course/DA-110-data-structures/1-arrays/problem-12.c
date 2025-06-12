/*
12. Write a program in C for adding two matrices of the same size.

Test Data :

Input the size of the square matrix (less than 5): 2

Input elements in the first matrix :

element - [0],[0] : 1

element - [0],[1] : 2

element - [1],[0] : 3

element - [1],[1] : 4

Input elements in the second matrix :

element - [0],[0] : 5

element - [0],[1] : 6

element - [1],[0] : 7

element - [1],[1] : 8

Expected Output :

The First matrix is :

1 2

3 4

The Second matrix is :

5 6

7 8

The Addition of two matrix is :

6 8

10 12
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