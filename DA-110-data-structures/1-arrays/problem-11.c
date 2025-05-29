/*
11. Write a program in C for a 2D array of size 3x3 and print the matrix.

Test Data :

Input elements in the matrix :

element - [0],[0] : 1

element - [0],[1] : 2

element - [0],[2] : 3

element - [1],[0] : 4

element - [1],[1] : 5

element - [1],[2] : 6

element - [2],[0] : 7

element - [2],[1] : 8

element - [2],[2] : 9

Expected Output :

The matrix is :

1 2 3

4 5 6

7 8 9
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