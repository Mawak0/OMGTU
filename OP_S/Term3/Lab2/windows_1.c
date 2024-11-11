#include <string.h>
#include <windows.h>
#include <stdio.h>
#include <fcntl.h>

int main()
{
    HANDLE hStdInput = GetStdHandle(STD_INPUT_HANDLE);
    HANDLE hStdOutput = GetStdHandle(STD_OUTPUT_HANDLE);
    char b1[] = "Enter any text: ";
    WriteFile(hStdOutput, b1, strlen((const char*)b1), NULL, NULL);
    char b2[30];
    ReadFile(hStdInput, &b2, 29, NULL, NULL);
    b2[29] = '\0';
    HANDLE hFile = CreateFile(L"test_file.txt", GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    WriteFile(hFile, b2, strlen((const char*)b2), NULL, NULL);
    CloseHandle(hFile);
}
