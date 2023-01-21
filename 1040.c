//media do aluno

#include <stdio.h>
 
int main() {
 
    double n1, n2, n3, n4, e, m;

    /*peso das notas
    n1 = 2
    n2 = 3 
    n3 = 4 
    n4 = 1
    */
 
 //ler as notas
    scanf("%lf %lf %lf %lf", &n1, &n2, &n3, &n4);

//calcular a media do aluno
    m = (n1*2+n2*3+n3*4+n4*1)/10;
//mostrar a media do aluno
    printf("Media: %.1f\n", m);
/* 
media >= 7.0 = aluno aprovado
media < 5 = aluno reprovado
media =>5 e <= 6.9 == aluno em exame
*/
   if (m >= 7.0){
        printf("Aluno aprovado.\n");
    }
    else if (m >= 5.0)
    {
        printf("Aluno em exame.\n");
        scanf("%lf", &e);
        printf("Nota do exame: %.1f\n", e);
        if (e + m / 2.0 > 5.0){
            printf("Aluno aprovado.\n");
        }
        else{
            printf("Aluno reprovado.\n");
        }
        printf("Media final: %.1f\n", (e + m ) / 2.0);
    }
    else{
        printf("Aluno reprovado.\n");
    }
    return 0;
}