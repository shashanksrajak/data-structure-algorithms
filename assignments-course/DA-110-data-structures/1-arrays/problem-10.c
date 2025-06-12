/*
10. Write a program in C to delete an element at a desired position from an array.

Test Data :

Input the size of array : 5

Input 5 elements in the array in ascending order:

element - 0 : 1

element - 1 : 2

element - 2 : 3

element - 3 : 4

element - 4 : 5

Input the position where to delete: 3

Expected Output :

The new list is : 1 2 4 5
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p;
    int size, position, index;

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

    while (1)
    {
        printf("Input the position where to delete : ");
        scanf("%d", &position);

        if ((position <= size && position >= 0))
        {
            break;
        }
        else
        {
            printf("Position out of bound!!!\n");
        }
    }

    index = position - 1;

    // O(1)
    if (size == 1 || index == size - 1)
    {
        p[index] = NULL;
    }
    else
    {
        // O(n)
        int i;
        for (i = index; i < size - 1; i++)
        {
            p[i] = p[i + 1];
        }
        p[i] = NULL;
    }

    printf("The new list is :");
    for (int i = 0; i < size; i++)
    {
        if (p[i] != NULL)
        {
            printf("%d ", p[i]);
        }
    }

    free(p);
    return 0;
}