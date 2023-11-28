# importar o método sample da biblioteca random
from random import sample

# lista com os 25 números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# sortear 15 números aleatórios dentre os 25 colocados na lista 'numeros'
sorteio = sample(numeros, 15)

# ordenar os 15 números em ordem crescente
sorteio.sort()

print(sorteio)