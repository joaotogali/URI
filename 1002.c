//Efetuar o cálculo da Área do circulo
#include <stdio.h>


int main (){

    //variáveis
    double r, area;

    //entrada de dados
    scanf("%lf",&r);

    //calculo
    area = 3.14159 * r * r;

    //saida
    printf("A=%.4lf\n", area);

    
return 0;
}