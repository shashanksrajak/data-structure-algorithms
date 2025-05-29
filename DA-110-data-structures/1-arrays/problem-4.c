/*
4. Write a program in C to copy the elements of one array into another array.

Test Data :

Input the number of elements to be stored in the array :3

Input 3 elements in the array :

element - 0 : 15

element - 1 : 10

element - 2 : 12

Expected Output :

The elements stored in the first array are :

15 10 12

The elements copied into the second array are :

15 10 12
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p, *q;
    int size;

    // take the size from the user
    printf("Input the number of elements to store in the array : ");
    scanf("%d", &size);

    // dynamically create a new array with input size
    p = (int *)malloc(size * sizeof(int));
    q = (int *)malloc(size * sizeof(int));

    // take the elements of array from user
    printf("Input %d number of elements in the array : ", size);

    for (int i = 0; i < size; i++)
    {
        printf("\nelement - %d ", i);
        scanf("%d", &p[i]);
    }

    // print the values
    printf("\nThe elements stored in the first array are :\n");

    for (int i = 0; i < size; i++)
    {
        printf("%d ", p[i]);
    }

    // copy elements into q
    for (int i = 0; i < size; i++)
    {
        q[i] = p[i];
    }

    printf("\nThe elements copied into the second array are :\n");
    for (int i = 0; i < size; i++)
    {
        printf("%d ", q[i]);
    }

    // free the memory
    free(p);
    free(q);

    return 0;
}