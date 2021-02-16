#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>

/* Ignore these functions */
void buffering() {
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void timeout(int sig) {
    if (sig == SIGALRM) {
        printf("[!] DOS Alert\n");
        _exit(0);
    }
}

void kill_signal() {
    signal(SIGALRM, timeout);
    alarm(60);
}

/*  Real challenge starts */

void oops() {
    FILE* f = fopen("flag.txt", "r");
    char flag[100];
    fscanf(f, "%s", flag);
    printf("%s\n", flag);
    fclose(f);
}


void hello() {
    char message[512];
    printf("I will say whatever you say back! try it!\n");
    fgets(message, 512, stdin);
    printf(message);
    exit(0);
}


void main(int argc, char* argv[]) {
    buffering();    // Ignore
    kill_signal();  // Ignore
    hello();
}
