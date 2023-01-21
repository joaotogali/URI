#include <stdio.h>
#include <math.h>

int main() {
    int l, ld, go = 1;
    char c, cd;
    
    scanf("%c%i %c%i", &c, &l, &cd, &ld);

    if ((abs(c-cd) == 2 && abs(l-ld) == 1) || (abs(c-cd) == 1 && abs(l-ld) == 2))
        go = 0;
    if (go)
        printf("IN");
        
    printf("VALIDO\n");
    
    return 0;
}