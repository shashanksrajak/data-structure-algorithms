#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void print(struct Node *ptr, int pos)
{
    if (ptr == NULL)
        return;

    if (pos % 2 == 1)
    {
        printf("%d", ptr->data);
        print(ptr->next, pos + 1);
    }
    if (pos % 2 == 0)
    {
        printf("%d", ptr->data);
    }
}

int main()
{

    // SLL - 1, 2, 3, 4, 5, 6, 7, 8
}
