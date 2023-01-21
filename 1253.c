#include <stdio.h>
#include <stdlib.h>
 
int main()
{
    int i, run = 0, repeat = 0, j = 0;
    char a[50];
    scanf("%d", &repeat);
    while(repeat--){
        scanf("%s", a);
        scanf("%d", &run);
        for (i = 0; i < 50; i++){
            if (a[i] == '\0')
                break;
            if ((a[i] - run) < 65)
                j = (a[i] - run) + 26;
            else
                j = a[i] - run;
        printf("%c", j);
        }
        printf("\n");
    }
    return 0;
}