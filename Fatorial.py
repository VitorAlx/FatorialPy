numeroFatorial = int(input("Digite o número (inteiro) a ser calculado seu fatorial: \n"))

total = 1

for i in range(numeroFatorial, 0, -1):
    total *= i

print(total)
