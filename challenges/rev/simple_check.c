#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void fail() {
    printf("[*] Wrong flag!\n");
    exit(0);
}

void success() {
    printf("[*] Correct flag!\n");
    exit(0);
}
 

int main() {

    printf("I will validate your flag!\n");
    char flag[50] = "HackRushCTF{";
    char input[50];
    printf("Submit your flag: ");
    scanf("%s", input);
    if(strlen(input) != 28) {
        fail();
    }
    for(int i = 0; i < 12; i++) {
        if(flag[i] != input[i]) {
            fail();
        }
    }
    if(input[12] != 120) {
        fail();
    }
    if(input[13] + input[14] != 110) {
        fail();
    }
    if(input[13] - input[14] != 2) {
        fail();   
    }
    if(input[15] != input[21]) {
        fail();
    }
    if(input[16] - input[14] != 48) {
        fail();
    }
    if(input[18] - input[17]*2 != 16) {
        fail();
    }
    if(input[18] + input[17] != 163) {
        fail();
    }
    if(input[20]*input[19] != 6148) {
        fail();
    }
    if(input[20] - input[19] != input[12]/2 + 3) {
        fail();
    }
    if(input[21] != 95) {
        fail();
    }
    if(input[24] != 109) {
        fail();
    }
    if(input[26] - input[22] != -53 ) {
        fail();
    }
    if(input[26] + input[22] != 179) {
        fail();
    }
    if(input[23] + 2 != input[25]) {
        fail();
    }
    if(input[23] + input[25] != 100) {
        fail();
    }
    if(input[27] != '}') {
        fail();
    }
    success();

}