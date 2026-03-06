inicio, fim = map(int, input("Digite o início e o fim do intervalo separados por espaço: ").split())
for i in range(inicio, fim):#RANGE
    
    def is_prime(num):
        if num < 2:
            return False
        for j in range(2, int(num**0.5) + 1):
            if num % j == 0:
                return False
        return True

    prime_sum = 0
    for i in range(inicio, fim + 1):
        if is_prime(i):
            prime_sum += i

    print(f"A soma dos números primos no intervalo de {inicio} a {fim} é: {prime_sum}")
    print(i)