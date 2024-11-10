#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


int main()
{
    int standart_input_d = 0;
    int standart_output_d = 1;
    char b1[] = "Enter any text (5 bytes): ";
    if (isatty(standart_input_d)){
        write(standart_output_d, b1, strlen((const char*)b1));
    }
    if (isatty(standart_output_d) == 0){
        int *outtty = open("/dev/tty", O_WRONLY);
        write(outtty, b1, strlen((const char*)b1));
    }

    char b2[6];
    read(standart_input_d, b2, 5);
    b2[5] = '\0';
    char b3[] = "This text was entered before: ";
    write(standart_output_d, b3, strlen((const char*)b3));
    write(standart_output_d, b2, strlen((const char*)b2));
}
