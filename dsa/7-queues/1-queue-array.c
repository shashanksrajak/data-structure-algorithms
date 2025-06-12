// Implement a Queue ADT using Arrays
#include <stdio.h>
#include <stdlib.h>

struct Queue
{
    int size;
    int front;
    int rear;
    int *Q; // pointer to Array
};

void enqueue(struct Queue *queue, int data)
{
    // add from rear
    if (queue->rear < queue->size - 1)
    {
        queue->rear++;
        queue->Q[queue->rear] = data;
    }
    return;
}

// pop out the first element FIFO
int dequeue(struct Queue *queue)
{
    if (queue->front == queue->rear)
    {
        // Queue is empty
        return -1;
    }
    else
    {
        // remove first element
        queue->front++;
        return queue->Q[queue->front];
    }
}

void display(struct Queue queue)
{
    for (int i = queue.front + 1; i < queue.size; i++)
    {
        printf("%d <--", queue.Q[i]);
    }
}

int main()
{
    struct Queue queue;
    queue.front = -1;
    queue.rear = -1;
    queue.size = 10; // this can be taken from user as well, we have taken a fixed size array for Queue
    queue.Q = (int *)malloc(sizeof(int) * queue.size);

    // Adding in the Queue
    int A[] = {12, 15, 14, 16, 26, 12, 99, 90, 21, 34};

    for (int i = 0; i < queue.size; i++)
    {
        enqueue(&queue, A[i]);
    }

    display(queue);

    printf("\nDequeue this element : %d", dequeue(&queue));

    printf("\nDequeue this element : %d", dequeue(&queue));

    printf("\nDequeue this element : %d", dequeue(&queue));

    printf("\nDequeue this element : %d", dequeue(&queue));

    printf("\nDequeue this element : %d", dequeue(&queue));
    printf("\nDequeue this element : %d", dequeue(&queue));
    printf("\nDequeue this element : %d", dequeue(&queue));
    printf("\nDequeue this element : %d", dequeue(&queue));
    printf("\nDequeue this element : %d", dequeue(&queue));
    printf("\nDequeue this element : %d", dequeue(&queue));
    printf("\nDequeue this element : %d", dequeue(&queue));

    return 0;
}
