#include <stdio.h>

int main(void) {
    int n;
    printf("Digite um número: ");
    scanf("%d", &n);

    int total = 0;
    for(int i = 0; i < n; i++) {
        total += i;
    }

    printf("A soma é %d\n", total);

    return 0;
}
