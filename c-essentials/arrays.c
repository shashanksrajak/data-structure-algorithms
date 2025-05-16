// Arrays in C

#include <stdio.h>

int main()
{
    // declare an array - datatype var name[size] - size is required!
    int A[5];
    // this array will hold garbage until intialized with some values

    // initialize the array
    A[1] = 100;
    A[2] = 102;

    for (int i = 0; i < 5; i++)
    {
        printf("%d\n", A[i]);
    }

    // declare & init an array
    int B[5] = {1, 3, 4, 5, 6};
    for (int i = 0; i < 5; i++)
    {
        printf("%d\n", B[i]);
    }

    // declare & init an array
    int C[5] = {1, 3, 4, 5, 6};
    for (int i = 0; i < 5; i++)
    {
        printf("%d\n", C[i]);
    }

    // what will it result?
    printf("%d\n", C[10]);

    return 0;
}