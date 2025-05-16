#include <stdio.h>
#include <stdlib.h>

int main()
{
    int A = 120934;
    char *p;

    p = &A; // p is 8 bytes so it can store addr of any dtype to which it points

    printf("Value of A var as read from pointer p is %d\n", *p);
    // note - the dtype of pointer should be of same type to which it is pointing
    // otherwise, when we try to read via this pointer, compiler will determine number of bytes to read from the dtype of pointer
    return 0;
}