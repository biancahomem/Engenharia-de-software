"""Exercício 02
Implementar uma solução em Python que resolva a seguinte questão:
-Se a nota for maior ou igual a 7, o estudante foi aprovado
-Se a nota for menor que 7 e maior ou igual a 5, o estudante está
em recuperação
-Se a nota for menor que 5, o estudante está reprovado"""

nota = eval(input("Digite a sua nota"))

if(nota>=7.0):
    resultado = "aprovado"
elif(nota>=5.0):
    resultado = "em recuperação"
else:
    rersultado = "reprovado"

print(f'O estudante está {resultado}') 