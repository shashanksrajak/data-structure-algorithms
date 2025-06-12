/*
8. Write a program in C to find the maximum and minimum elements in an array.

Test Data :

Input the number of elements to be stored in the array :3

Input 3 elements in the array :

element - 0 : 45

element - 1 : 25

element - 2 : 21

Expected Output :

Maximum element is : 45

Minimum element is : 21
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

    // max element
    int max = p[0], min = p[0];

    for (int i = 0; i < size; i++)
    {
        if (p[i] > max)
        {
            max = p[i];
        }
        if (p[i] < min)
        {
            min = p[i];
        }
    }

    printf("Maximum element : %d\n", max);
    printf("Minimum element : %d", min);

    free(p);

    return 0;
}