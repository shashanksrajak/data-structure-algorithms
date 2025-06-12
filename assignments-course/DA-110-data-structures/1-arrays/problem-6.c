/*

6. Write a program in C to print all unique elements in an array.

Test Data :

Print all unique elements of an array:

------------------------------------------

Input the number of elements to be stored in the array: 4

Input 4 elements in the array :

element - 0 : 3

element - 1 : 2

element - 2 : 2

element - 3 : 5

Expected Output :

The unique elements found in the array are:

3 5
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

    printf("The unique elements found in the array are:\n");
    for (int i = 0; i < size; i++)
    {
        int unique = 1;
        for (int j = 0; j < size; j++)
        {
            if (p[i] == p[j] && i != j)
            {
                unique = 0;
            }
        }

        if (unique == 1)
        {
            printf("%d ", p[i]);
        }
    }

    return 0;
}