// Create a linked list and traverse it

#include <stdio.h>
#include <stdlib.h>

// struct for linked list Node
struct Node
{
    int data;
    struct Node *next;
} *first; // we create a struct and also init a first pointer with struct Node type

void create(int A[], int n)
{
    int i;
    struct Node *t, *last;

    first = (struct Node *)malloc(sizeof(struct Node));
    first->data = A[0];
    first->next = NULL;
    last = first;

    // other elements we create with for loop
    for (i = 1; i < n; i++)
    {
        // create a new node and point last->next to this new node
        t = (struct Node *)malloc(sizeof(struct Node));
        t->next = NULL;
        t->data = A[i];

        last->next = t;
        last = t;
    }
}

void display(struct Node *first)
{
    struct Node *p = first;

    while (p != NULL)
    {
        printf("%d --> ", p->data);
        p = p->next;
    }
}

void display_recursively(struct Node *p)
{
    if (p != NULL)
    {
        printf("%d --> ", p->data);
        display_recursively(p->next);
    }
}

void display_recursively_reverse(struct Node *p)
{
    if (p != NULL)
    {
        display_recursively_reverse(p->next);
        printf("%d --> ", p->data);
    }
}

int main()
{
    int A[] = {10, 3, 5, 7, 12, 15};

    create(A, 6);
    display(first);

    printf("\nDisplaying recursively--- \n");
    display_recursively(first);

    printf("\nDisplaying recursively in reverse order--- \n");
    display_recursively_reverse(first);
    return 0;
}
