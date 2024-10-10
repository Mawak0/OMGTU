#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

int main()
{
    int standart_input_d = 0;
    int standart_output_d = 1;
    int handle1 = open("test_file", O_RDONLY);
    int handle2 = dup(handle1);
    int handle3 = open("test_file", O_RDONLY);
    lseek(handle1, 10, 0);
    printf("%d\n", handle1);
    printf("%d\n", handle2);
    printf("%d\n", handle3);
    char b1[8];
    char b2[8];
    char b3[8];
    read(handle1, b1, 7);
    read(handle2, b2, 7);
    read(handle3, b3, 7);
    printf(b1);
    printf("\n");
    printf(b2);
    printf("\n");
    printf(b3);
    printf("\n");




}
