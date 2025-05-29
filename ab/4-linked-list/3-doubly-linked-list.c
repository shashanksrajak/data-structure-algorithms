// Create a linked list and traverse it

#include <stdio.h>
#include <stdlib.h>

// struct for linked list Node
struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
} *first; // we create a struct and also init a first pointer with struct Node type

void create(int A[], int n)
{
    int i;
    struct Node *t, *last;

    first = (struct Node *)malloc(sizeof(struct Node));
    first->data = A[0];
    first->next = NULL;
    first->prev = NULL;
    last = first;

    // other elements we create with for loop
    for (i = 1; i < n; i++)
    {
        // create a new node and point last->next to this new node
        t = (struct Node *)malloc(sizeof(struct Node));
        t->next = NULL;
        t->prev = NULL;
        t->data = A[i];

        last->next = t;
        t->prev = last;
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

int main()
{
    int A[] = {10, 3, 5, 7, 12, 15};

    create(A, 6);
    display(first);

    printf("\nDisplaying list--- \n");

    return 0;
}
