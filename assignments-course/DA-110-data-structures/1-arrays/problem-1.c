// 1. Write a program in C to store elements in an array and print them.
/*
Test Data :

Input 10 elements in the array :

element - 0 : 0

element - 1 : 1

element - 2 : 2

.......

Expected Output :

Elements in array are: 0 1 2 3 4 5 6 7 8 9
*/

#include <stdio.h>

int main()
{
    int size = 10;
    int A[size];

    // scan input from user
    printf("Input 10 elements in the array :\n");
    for (int i = 0; i < size; i++)
    {
        printf("\nelement - %d :", i);
        scanf("%d", &A[i]);
    }

    // print the elements of array
    printf("Elements in array are: ");

    for (int i = 0; i < size; i++)
    {
        printf("%d ", A[i]);
    }

    return 0;
}