/*
5. Write a program in C to count the total number of duplicate elements in an array.

Test Data :

Input the number of elements to be stored in the array :3

Input 3 elements in the array :

element - 0 : 5

element - 1 : 1

element - 2 : 1

Expected Output :

Total number of duplicate elements found in the array is : 1

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

    int duplicates = 0;
    for (int i = 0; i < size; i++)
    {
        // check if this element is already processed
        int already_counted = 0;
        for (int k = i - 1; k >= 0; k--)
        {
            if (p[i] == p[k])
            {
                // already proceesed; do not execute further logic
                already_counted = 1;
                break;
            }
        }

        if (already_counted)
        {
            continue;
        }

        for (int j = i + 1; j < size; j++)
        {
            if (p[i] == p[j])
            {
                duplicates++;
                break;
            }
        }
    }

    printf("\nTotal number of duplicate elements found in the array is : %d", duplicates);

    // free the memory
    free(p);

    return 0;
}