/*

7. Write a program in C to count the frequency of each element of an array.

Test Data :

Input the number of elements to be stored in the array :3

Input 3 elements in the array :

element - 0 : 25

element - 1 : 12

element - 2 : 43

Expected Output :

The frequency of all elements of an array :

25 occurs 1 times

12 occurs 1 times

43 occurs 1 times
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

    printf("The frequency of all elements of an array :\n");
    for (int i = 0; i < size; i++)
    {
        int frequency = 1;
        for (int j = 0; j < size; j++)
        {
            if (p[i] == p[j] && i != j)
            {
                frequency++;
            }
        }

        printf("%d occurs %d times\n", p[i], frequency);
    }

    return 0;
}