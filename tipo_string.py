"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
O mais comum em python é utilizar àspas simples 
"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

# Utilizar o upper para deixar todos em maísculo
print(nome.upper())

# Utilizar o lower para deixar todos em minúsculo
print(nome.lower())

print(nome.split()) # Transforma em uma lista de string


# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']


nome = 'Geek University'
print(nome[0:4]) # Slice de string
print(nome[5:15]) # Slice de string

print(nome.split()[0])

print(nome.split()[1])

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) # Inversão da string

print(nome.replace('e','i'))

texto = 'socorram me subino onibus em marrocos' #Palíndromo
print(texto)
print(texto[::-1]) # Inversão da string
