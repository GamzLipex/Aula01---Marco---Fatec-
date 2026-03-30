#include <stdio.h>
#include <stdlib.h>

int main() {
    int num;

    printf("Digite um num inteiro positivo: ");
    scanf("%d", &num);

    printf("O dobro do seu num e: %d\n", num * 2);
    printf("A metado do num e: %.2f\n", num / 2.0);

    if (num % 2 == 0) {
        printf("O num e par.\n");
    } else {
        printf("O num e impar.\n");
    }
    
    printf("Tabuada\n");
    
    int multi = 1;
    for(multi = 1; multi <= 10; multi++){
    	printf("%d x %d = %d\n", multi, num, num * multi);
	}

    return 0;
}

