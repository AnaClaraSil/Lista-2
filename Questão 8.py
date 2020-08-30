preco1 = float(input('Insira o primeiro preço'))
preco2 = float(input('Insira o segundo preço'))
preco3 = float(input('Insira o terceiro preço'))

menor = 0
if(preco1<preco2 and preco2<preco3):
	menor = preco1
if(preco1<preco2 and preco1<preco3):
	menor = preco1
if(preco1>preco2 and preco2<preco3):
	menor = preco2
if(preco1>preco2 and preco2>preco3):
	menor = preco3

print('O melhor produto para comprar é o que tem o valor de', menor)