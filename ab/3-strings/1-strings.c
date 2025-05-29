// Define a char data type and understand how it is stored and read by compiler
// Understand strings which are array of chars
// String manipulation

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char A = 'A'; // "S" will raise warning

    char B = 'B';

    printf("Value stored in A is %d\n", A);
    printf("Value in A is %c\n", A);

    // int C = A + 2;
    char C = A + 2;

    printf("Value stored in C is %d\n", C);
    printf("Value in C is %c\n", C);

    // strings
    char user_name[] = "Shashank Rajak";
    char *password;

    printf("User name is %s\n", user_name);

    password = "Shashank";

    int len = 0;
    for (int i = 0; user_name[i] != '\0'; i++)
    {
        len++;
    }

    printf("Length of above string is %d\n", len);

    printf("%s\n", password);

    if (password[8] == '\0')
    {
        printf("end");
    }
    else
    {
        printf("no");
    }

    return 0;
}