#include <windows.h>
#include <stdio.h>
#include <string.h>

void setColor(WORD color) {
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(hConsole, color);
}

void printCentered(const char* message, WORD color) {
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);

    GetConsoleScreenBufferInfo(hConsole, &csbi);
    int consoleWidth = csbi.srWindow.Right - csbi.srWindow.Left + 1;
    int consoleHeight = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;

    COORD cursorPosition;
    cursorPosition.X = (consoleWidth - strlen(message)) / 2;
    cursorPosition.Y = consoleHeight / 2;

    SetConsoleCursorPosition(hConsole, cursorPosition);
    setColor(color);
    printf("%s\n", message);
    setColor(FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED);
}

int main() {
    HANDLE hFile;
    DWORD bytesRead;
    char buffer[1024];
    const char* fileName = L"test.txt";

    while (1) {
        hFile = CreateFile(fileName, GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

        if (hFile == INVALID_HANDLE_VALUE) {
            DWORD error = GetLastError();
            if (error == ERROR_SHARING_VIOLATION) {
                printCentered("File is currently in use by another process. Waiting...", FOREGROUND_RED);
                Sleep(3000);
                continue;
            }
            else if (error == ERROR_FILE_NOT_FOUND) {
                printCentered("File not found!", FOREGROUND_RED);
                return 1;
            }
            else {
                printCentered("Error opening file.", FOREGROUND_RED);
                return 1;
            }
        }
        else {
            printCentered("File opened successfully!", FOREGROUND_GREEN);
            break;
        }
    }

    if (ReadFile(hFile, buffer, sizeof(buffer) - 1, &bytesRead, NULL)) {
        buffer[bytesRead] = '\0';
        printf(buffer);
    }
    else {
        printCentered("Error reading file.", FOREGROUND_RED | FOREGROUND_INTENSITY);
    }

    CloseHandle(hFile);
    printf("Press any key...\n");
    getchar();
    return 0;
}
