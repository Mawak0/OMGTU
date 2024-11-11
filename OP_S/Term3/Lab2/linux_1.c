#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

int main()
{
    int standart_input_d = 0;
    int standart_output_d = 1;
    char b1[] = "Enter any text: ";
    write(standart_output_d, b1, strlen((const char*)b1));
    char b2[30];
    read(standart_input_d, b2, 29);
    b2[29] = '\0';
    int file = open("test_file", O_CREAT | O_WRONLY | O_TRUNC);
    write(file, b2, strlen((const char*)b2));
    close(file);
}
