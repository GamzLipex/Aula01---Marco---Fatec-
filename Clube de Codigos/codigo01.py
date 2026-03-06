inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

def primo(num):
    if num < 2:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

primos = [i for i in range(inicio, fim + 1) if primo(i)]


if primos:
    print(f"Primeiro número primo: {primos[0]}")
    print(f"Último número primo: {primos[-1]}")
    print(f"Soma dos números primos: {sum(primos)}")
else:
    print("Nenhum número primo encontrado no intervalo.")
    
