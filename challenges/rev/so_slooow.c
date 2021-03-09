#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define ll long long
ll p = 1000000000 + 7; 


int flag[32] = {272258510, 272263388, 272263390, 272268191, 272268198, 272273246, 272273240, 272278026, 272278049, 272283085, 272283103, 272287915, 272287892, 272292919, 272292969, 272297802, 272297825, 272302659, 272302599, 272307673, 272307672, 272312528, 272312508, 272317564, 272317482, 272322339, 272322354, 272327355, 272327383, 272332174, 272332235, 272337035}; 

void kill_it() {
    printf("Your machine is too slow\n");
    _exit(0);
}


void processing() {
    printf("......\n");
}

void handle_timing() {
    signal(SIGALRM, kill_it);
    alarm(4);
}

ll fof(ll value) {
    if(value <= 3) {
        return value;
    }
    processing();
    sleep(1);
    return (fof(value - 1) + fof(value - 3))%p;
}

ll get_the_key() {
    ll value = 0x1337;
    return fof(value);
}

char* decrypt_flag(ll key) {
    char* str_flag = malloc(32);
    for(int i = 0; i < 32; i++) {
        str_flag[i] = (char)(flag[i]^key)%256;
        if(i%2 == 0) {
            key += 0x1337;
        }
    }
    return str_flag;
} 

void show_the_flag(ll key) {
    printf("The flag is %s\n", decrypt_flag(key));
}


int main() {
    printf("Let's check if your computer can handle heavy computation...\n");
    printf("I will now print the flag\n");
    handle_timing();
    show_the_flag(get_the_key());
    printf("Nice\n");

}