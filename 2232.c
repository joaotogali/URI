#include <stdio.h>
#include <math.h>

int main(){
    int a, b;
    
    scanf("%i", &a);

    while (a--) {

        scanf("%i", &b);
        printf("%i\n", (int) pow(2, b) - 1);

    }

    return 0;
}