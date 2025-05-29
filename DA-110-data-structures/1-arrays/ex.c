#include <stdio.h>

int main()
{
    int a[3][4] = {{3, 2, 1}, {6, 5, 4}};

    printf("%u", sizeof(int));

    printf("%u, %u, %u\n", a, a + 1, a + 3);

    return 0;
}