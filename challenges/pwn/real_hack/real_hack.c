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

void login() {
    char password[50];
    printf("\nWhere is the flag anyway?\n");
    gets(password);
    if(strcmp(password, "1337_H4cker") == 0) {
        printf("You are logged in!\n");
    } else {
        printf("Wrong password!\n");
    }
    printf(password);
}


void main(int argc, char* argv[]) {
    buffering();    // Ignore
    kill_signal();  // Ignore
    login();
    login();    // Try again maybe?
    
}
