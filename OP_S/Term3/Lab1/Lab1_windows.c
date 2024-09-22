
#include <windows.h>
#include <stdio.h> 
#include <locale.h>


// exe <input.txt >output.txt

int main()
{
    char* locale = setlocale(LC_ALL, "");
    HANDLE standart_input_d;
    standart_input_d = GetStdHandle(STD_INPUT_HANDLE);
    printf("Значение хендла стандартного ввода: %p \n", standart_input_d);
    fflush(stdout);
    HANDLE standart_output_d;
    standart_output_d = GetStdHandle(STD_OUTPUT_HANDLE);
    printf("Значение хендла стандартного вывода: %p \n", standart_output_d);
    fflush(stdout);
    LPCVOID b1 = "Enter any text (5 bytes): ";
    WriteFile(standart_output_d, b1, strlen((const char*)b1), NULL, NULL);
    char b2[6];
    DWORD bytes_read = 0;
    ReadFile(standart_input_d, &b2, 5, &bytes_read, NULL);
    b2[bytes_read] = '\0';
    LPCVOID b3 = "This text was entered before: ";
    WriteFile(standart_output_d, b3, strlen((const char*)b3), NULL, NULL);
    WriteFile(standart_output_d, b2, strlen((const char*)b2), NULL, NULL);
}
