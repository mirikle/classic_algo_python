#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char** argv){
	if(argc != 3){
		perror("Usage: mycp file1 file2");
		exit(-1);
	}
	printf("%s\n", argv[1]);
	printf("%s\n", argv[2]);
	int f1 = open(argv[1], O_RDONLY);
	int f2 = open(argv[2], O_WRONLY | O_CREAT, 0644);
	if(f1 == -1 || f2 == -1){
		perror("File open error!");
		exit(-1);
	}
	char buf[1024];
	while(1){
		int length = read(f1, buf, sizeof(buf));
		if(length == 0){
			printf("Completed!\n");
			break;
		}
		else if(length == -1){
			printf("File reading error!\n");
			break;
		}
		else{
			if(write(f2, buf, length) != length){
				perror("File writting error!\n");
				exit(1);
			}
		}
	}
	if(close(f1)){
		printf("File 1 close error!\n");
		exit(-1);
	}
	if(close(f2)){
		printf("File 2 close error!\n");
		exit(-1);
	}
	return 0;
}
