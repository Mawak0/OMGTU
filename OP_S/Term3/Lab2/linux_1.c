#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

int main()
{
    int standart_input_d = 0;
    int standart_output_d = 1;
    char b1[] = "Enter any text (15 bytes): ";
    write(standart_output_d, b1, strlen((const char*)b1));
    char b2[16];
    read(standart_input_d, b2, 15);
    b2[15] = '\0';
    int file = open("test_file", "w");
    printf("%d", file);
    int status = 1;
    status = write(file, b2, strlen((const char*)b2));
    printf("%d", status);
    close(file);
}
