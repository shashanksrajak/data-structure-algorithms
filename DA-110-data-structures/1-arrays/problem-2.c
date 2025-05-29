/*
2. Write a program in C to read n number of values in an array and display them in reverse order.

Test Data :

Input the number of elements to store in the array :3

Input 3 number of elements in the array :

element - 0 : 2

element - 1 : 5

element - 2 : 7

Expected Output :

The values stored in the array are :2 5 7

The values stored in the array in reverse are :7 5 2

*/
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p;
    int size;

    // take the size from the user
    printf("Input the number of elements to store in the array : ");
    scanf("%d", &size);

    // dynamically create a new array with input size
    p = (int *)malloc(size * sizeof(int));

    // take the elements of array from user
    printf("Input %d number of elements in the array : ", size);

    for (int i = 0; i < size; i++)
    {
        printf("\nelement - %d ", i);
        scanf("%d", &p[i]);
    }

    // print the values
    printf("\nThe values stored in the array are : ");

    for (int i = 0; i < size; i++)
    {
        printf("%d ", p[i]);
    }

    printf("\nThe values stored in the array in reverse are");
    for (int i = size - 1; i >= 0; i--)
    {
        printf("%d ", p[i]);
    }

    return 0;
}