#include <stdio.h>

int main()
{
    // define a struct
    struct Rectangle
    {
        int length;
        int breadth;
        char c;
    };

    // declare & init a struct variable
    struct Rectangle R = {10, 5};

    printf("%lu", sizeof(R));

    printf("struct members => %d %d", R.length, R.breadth);

    return 0;
}