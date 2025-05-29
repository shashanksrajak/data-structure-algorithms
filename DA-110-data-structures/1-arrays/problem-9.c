/*
9. Write a program in C to separate odd and even integers into separate arrays.

Test Data :

Input the number of elements to be stored in the array :5

Input 5 elements in the array :

element - 0 : 25

element - 1 : 47

element - 2 : 42

element - 3 : 56

element - 4 : 32

Expected Output :

The Even elements are :

42 56 32

The Odd elements are :

25 47
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p, *odd, *even;
    int size;

    // take the size from the user
    printf("Input the number of elements to store in the array : ");
    scanf("%d", &size);

    // dynamically create a new array with input size
    p = (int *)malloc(size * sizeof(int));
    odd = (int *)malloc(size * sizeof(int));
    even = (int *)malloc(size * sizeof(int));

    // take the elements of array from user
    printf("Input %d number of elements in the array : ", size);

    for (int i = 0; i < size; i++)
    {
        printf("\nelement - %d ", i);
        scanf("%d", &p[i]);
    }

    // odd and even elements

    int i = 0, j = 0, k = 0; // j - even; k - odd

    for (i = 0; i < size; i++)
    {
        // check if its even
        if (p[i] % 2 == 0)
        {
            even[j] = p[i];
            j++;
        }
        else
        {
            odd[k] = p[i];
            k++;
        }
    }

    printf("\nThe Even elements are :\n ");
    for (int a = 0; a < j; a++)
    {
        printf("%d ", even[a]);
    }

    printf("\nThe Odd elements are :\n ");
    for (int a = 0; a < k; a++)
    {
        printf("%d ", odd[a]);
    }

    free(p);
    free(odd);
    free(even);

    return 0;
}