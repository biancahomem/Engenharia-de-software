"""Exercício 03
implementar uma solução em Python que resolva a seguinte questão:
-Calcular o valor de uma compra, sendo que o preço unitário é de R$10

-Se for feita uma compra de até 10 unidades, não há descontos
-Para compras entre 11 e 20 unidades é dado um desconto de 10%
-Acima de 20 unidades, é dado um desconto de 20%"""

unidade = 10.00
desconto10 = 0.1
desconto20 = 0.2

quantidade = eval(input('Digite a quantidade que vai comprar: '))
if(quantidade <= 10): #menor ou igual a 10
    valorf = unidade*quantidade
elif(quantidade <= 20):
    valorf = unidade*quantidade*(1-desconto10)
else:
    valorf = unidade*quantidade*(1-desconto20)

    print(f'O valor final da compra é')