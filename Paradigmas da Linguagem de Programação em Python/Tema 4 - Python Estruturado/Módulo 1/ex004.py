"""Exercício 04
implementarr uma solução em python que some todos os números pares
de uma lista

por exemplo, se a lista forr [10, 2, 5, 7, 6, 3], o resultado deve
ser igual a 18."""

#estratégia 01

lista = [10, 2, 5, 7, 6, 3]
n=len(lista) #calcula o comprimento da lista
soma=0
for i in range(n): #varre a lista dentro do intervalo
    if(lista[i]%2==0): #pega o índice i
        soma=soma+lista[i]
print(f'O somatório dos elementos pares da lista é: {soma}')

#estratégia 02 - anotação de progração funcional

lista = [10, 2, 5, 7, 6, 3]

soma=0
for num in lista: #pega os elementos da lista, facilitando a anotação
    if(num%2==0):
        soma=soma+num
print(f'O somatório dos elementos pares da lista é: {soma}')