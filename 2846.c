#include <stdio.h>
#include <math.h>

int Fib(long long n) {
    long long r1 = 5 * n * n + 4;
    long long r2 = 5 * n * n - 4;
    long long a = sqrt(r1);
    long long b = sqrt(r2);
    return a * a == r1 || b * b == r2;
}

int main() {
    long long n, i = 1, r = 0;
    while (scanf("%lld", &n) != EOF) {
        while (n >= i) {
            if (!Fib(++r)) {
                i++;
            }
        }
        printf("%lld\n", r);
    }

    return 0;
}