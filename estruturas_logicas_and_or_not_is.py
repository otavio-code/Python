"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True.
Para o 'is', o valor é comparado com um segundo
"""

ativo = False
logado = False

if ativo and logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


if ativo or logado:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!')

print(not False)
print(not True)

if ativo is True:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


# ativo é True?
print(ativo is True)

"""
1 == 1
True
1 is 1
True
"""