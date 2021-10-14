"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)


nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista


# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range (valor_inicial, valor_final)
OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista



Enumerate: 
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'))


OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

for _, indice, letra in enumerate(nome):
    print(letra)

for indice, letra in enumerate(nome):
    print(letra)




# Na posição 0 vai trazer os números e na posição 1 vai trazer as letras
for valor in enumerate(nome):
    print(valor[0])


for valor in enumerate(nome):
    print(valor[1])


qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num

print(f'A soma é {soma}')

"""

nome = 'Geek University'
for letra in nome:
    print(letra, end='')


# Orginal: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'

for x in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)








