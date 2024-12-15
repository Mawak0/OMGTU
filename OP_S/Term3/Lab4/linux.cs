#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>

void Message(char message[], int color) {
    struct winsize w;
    ioctl(1, TIOCGWINSZ, &w);
    int rows = w.ws_row;
    int cols = w.ws_col;

    int message_length = strlen(message);
    int start_row = rows / 2;
    int start_col = (cols - message_length) / 2;
    printf("\033[2J");
    printf("\033[%d;%dH\033[%dm%s\033[0m", start_row, start_col, color, message);
    printf("\033[%d;0H", rows + 1);
}


int main()
{
	char file_to_open[] = "file.txt";
	int file = open(file_to_open, O_RDONLY);
	if (file == -1){
		Message("Error opening file", 31);
		return 0;
	}
	struct stat st;
	fstat(file, &st);
	long size = st.st_size;
	struct flock lock;
	lock.l_type = F_WRLCK;
	lock.l_start = 0;
	lock.l_len = size;
	int block = fcntl(file, F_SETLK, lock);
	if (block == -1){
		Message("File blocking failed, waiting...", 31);
		int block = fcntl(file, F_SETLKW, lock);
	}
	Message("File blocked successfully", 32);
	char file_content[size+1];
	file_content[size] = '\0';
	int r = read(file, file_content, size);
	printf(file_content);
	sleep(7);
}
