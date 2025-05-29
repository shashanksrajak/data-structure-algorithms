// How to increase the size of the array

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *p, *q;

    p = (int *)malloc(sizeof(int) * 5);
    q = (int *)malloc(sizeof(int) * 10);

    p[0] = 1, p[1] = 2, p[2] = 4, p[3] = 18, p[4] = 10;

    // copy p to q
    for (int i = 0; i < 5; i++)
    {
        q[i] = p[i];
    }

    // free p
    free(p);

    // point p to q (increased size array)
    p = q;

    q = NULL;

    return 0;
}