/*
3. Write a program in C to find the sum of all elements of the array.

Test Data :

Input the number of elements to be stored in the array :3

Input 3 elements in the array :

element - 0 : 2

element - 1 : 5

element - 2 : 8

Expected Output :

Sum of all elements stored in the array is : 15
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
    printf("\nSum of all elements stored in the array is :");
    int sum = 0;

    for (int i = 0; i < size; i++)
    {
        sum = sum + p[i];
    }

    printf("%d", sum);

    return 0;
}