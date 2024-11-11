#include <string.h>
#include <windows.h>
#include <stdio.h>

int main()
{
    DWORD bytesRead;
    char b1[8] = { 0 };
    char b2[8] = { 0 };
    char b3[8] = { 0 };

    HANDLE handle1 = CreateFile(L"test_file.txt", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    HANDLE handle2;
    DuplicateHandle(GetCurrentProcess(), handle1, GetCurrentProcess(), &handle2, 0, FALSE, DUPLICATE_SAME_ACCESS);
    HANDLE handle3 = CreateFile(L"test_file.txt", GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

    SetFilePointer(handle1, 10, NULL, FILE_BEGIN);

    printf("%p\n", handle1);
    printf("%p\n", handle2);
    printf("%p\n", handle3);

    ReadFile(handle1, b1, 7, &bytesRead, NULL);
    ReadFile(handle2, b2, 7, &bytesRead, NULL);
    ReadFile(handle3, b3, 7, &bytesRead, NULL);

    printf("%s\n", b1);
    printf("%s\n", b2);
    printf("%s\n", b3);

    CloseHandle(handle1);
    CloseHandle(handle2);
    CloseHandle(handle3);

    return 0;
}
