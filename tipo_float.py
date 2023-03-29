"""
Tipo Float

Tipo real, decimal

Casas decimais 

OBS: O separador de casas decimais na programção é um ponto e não uma vírgula.

"""

#Errado do ponto de vista do Float, mas gera uma tupla
valor = 1,44
print(type(valor))

#Certo do ponto de vista Float
valor = 1.44
print(type(valor))

# É possível
valor1, valor2 = 1, 44

print(valor1)
print(valor2)

# Podemos converter um float para um int

#OBS: Ao converter valores float para inteiros, nós perdemos precisão

res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos

variavel=4j
print(variavel)
print(type(variavel))
variavel -= 5
print(variavel)

# É possível converter valores inteiro para float

num = 3
print(float(num))
print(type(num))
