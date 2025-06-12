// Abstract Data Type for Arrays

#include <stdio.h>
#include <stdlib.h>

// Array Data Type
struct Array
{
    // int *A;    // for dynamic array
    int A[20]; // for static array
    int size;
    int length; // length <= size at any given time
};

void Display(struct Array arr)
{
    printf("\nElements in the array are:\n");
    for (int i = 0; i < arr.length; i++)
    {
        printf("%d\n", arr.A[i]);
    }
}

void Append(struct Array *arr, int x)
{
    if (arr->length < arr->size)
    {
        arr->A[arr->length++] = x;
    }
}

void Insert(struct Array *arr, int index, int element)
{
    if (index >= 0 && index <= arr->length)
    {
        for (int i = arr->length; i > index; i--)
        {
            arr->A[i] = arr->A[i - 1];
        }
        arr->A[index] = element;
        arr->length++;
    }
}

int main()
{
    // for simplicity lets take a static array, we can also use malloc for dynamic arrays
    struct Array arr = {{10, 20, 30, 40, 50}, 20, 5}; // define and initialize

    // print this array
    Display(arr);

    // append
    Append(&arr, 60);

    return 0;
}