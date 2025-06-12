// Implement arrays in c

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nums[5]; // declaring an array of size 5 which will contain int elements

    int marks[] = {100, 95, 99, 99, 96};

    float scores[10];

    for (int i = 0; i < 10; i++)
    {
        scores[i] = (float)i * 2.1;
    }

    printf("nums[0] : %d\n", nums[0]);
    printf("marks[0] : %d\n", marks[0]);
    printf("marks[0] : %f\n", scores[1]);

    return 0;
}