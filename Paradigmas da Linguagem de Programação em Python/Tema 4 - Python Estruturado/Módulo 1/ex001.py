"""Exercício 01
Implementar uma solução em Python que verifique se um número
é par ou ímpar"""

x = eval(input("Insira um númeo")) #eval transforma a strring em número
y = x%2
if(y==0):
    y = "par"
else:
    y = "ímpar"
print(f'O valor digitado é {y}')