"""
Escopo de variáveis

Dois casos de escopo:

1- Variaveis globais;
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
2- Variaveis locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.


Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da variavel
Python é uma linguagem de tipagem dinâmica. Isso significa
que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java;
int numero =42;
"""
numero = 42
print(numero)
print(type(numero))



