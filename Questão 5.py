nota1 = float(input('Insira a primeira nota '))
nota2 = float(input('Insira a segunda nota '))
media = (nota1 + nota2)/ 2
resul = ''
if (media == 7 or media > 7):
	resul = 'Aprovado'
if (media < 7):
	resul = 'Reprovado'
if (media == 10):
	resul= 'Aprovado com Distinção'

print('A media foi', media)
print('Voce foi', resul)
