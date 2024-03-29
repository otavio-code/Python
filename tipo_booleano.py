"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constante, Verdadeiro ou Falso

True -> Verdadeiro
Falase -> Falso

Errado:
true, false

Certo:
True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro, o resultado será falso,
se for falso o resultado será verdadeiro. Ou seja, sempre contrário.
"""

print(not ativo)

# Ou (or)

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
not ativo
logado = False

print(ativo or logado)


# E (and):

"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos valores devem ser verdadeiro.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""
