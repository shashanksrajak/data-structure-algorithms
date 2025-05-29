// circular linked list

#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
} *Head;

void create(int A[], int n)
{
    int i;
    struct Node *t, *last;

    Head = (struct Node *)malloc(sizeof(struct Node));

    Head->data = A[0];
    Head->next = Head; // point to Head itself, circular
    last = Head;

    for (i = 1; i < n; i++)
    {
        t = (struct Node *)malloc(sizeof(struct Node));

        t->data = A[i];
        t->next = last->next;

        last->next = t;
        last = t;
    }
}

void display(struct Node *head)
{
    struct Node *p = head;

    do
    {
        printf("%d -> ", p->data); // this block gets executed first then while is checked
        p = p->next;

    } while (p != head); // if we do not stop traversal at Head, then the list will keep on circulating.
}

int main()
{
    int A[] = {4, 5, 10, 2, 12, 99};
    create(A, 6);
    display(Head);
    return 0;
}