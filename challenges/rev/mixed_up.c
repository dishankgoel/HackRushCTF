#include<stdlib.h>
#include<stdio.h>
#include<string.h>

// char* flag = "\xbe\xcc\xb6\x0c\xce\xcc\xee,\xfa\x9e\x84\xaeN*\xfa\xce\x8c\xfa,N&\x8c\x16\xe2\xdeb*\xc2\x16\xce\xaeJ\xd6\xc6\x86\x12";
int flag[50] = {190, 204, 182, 12, 206, 204, 238, 44, 250, 158, 132, 174, 78, 42, 250, 206, 140, 250, 44, 78, 38, 140, 22, 226, 222, 98, 42, 194, 22, 206, 174, 74, 214, 198, 134, 18};

int mixup(int d) {
    int ans = 0;
    for(int i = 0; i < 4; i++) {
        ans = ans | (((1 << i)&d) << (7 - 2*i))&255;
    }
    for(int i = 4; i < 8; i++) {
        ans = ans | (((1 << i)&d) >> (2*i - 7))&255;
    }
    return (ans + 256)%256;
}



int check_flag(char* input) {
    int encrypted[50];
    if(strlen(input) != 36) {
        return 0;
    }
    for(int i = strlen(input) - 1; i >= 0; i--) {
        encrypted[strlen(input) - 1 - i] = mixup(input[i]);
    }
    int ans = 1;
    for(int i = 0; i < strlen(input); i++) {
        if(encrypted[i] != flag[i]) {
            ans = 0;
            break;
        }
    }
    return ans;
}


int main() {
    char input[50];
    printf("Submit the flag: ");
    scanf("%s", input);
    if(check_flag(input) == 1) {
        printf("[*] Correct!\n");
    } else {
        printf("[*] Wrong!\n");
    }
    exit(0);
}