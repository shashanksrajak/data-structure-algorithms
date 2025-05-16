#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A = 10;
    // define a pointer
    int *p;

    // init the pointer
    // p = A; // store value of A in p; compiler will give warning but noone is stopping to store value of A in p
    p = &A; // store addr of A in p; right way to do it

    printf("Value of pointer p is %d\n", *p); // dereference p -> print value of A

    // pointers and arrays
    int nums[5] = {2, 3, 4, 5, 6};
    int *ptr;
    ptr = nums; // no need for &nums because nums itself stores address of nums[0]
    // ptr = &nums[0] // other way to write it

    printf("Value of pointer ptr is %d\n", ptr[2]);

    // allocating in heap memory
    int *ptrA;
    ptrA = (int *)malloc(5 * sizeof(int));
    printf("Value of pointer ptrA is %d\n", ptrA);
    free(ptrA);

    return 0;
}