num1 = float(input('Insira o primeiro número'))
num2 = float(input('Insira o segundo número'))
num3 = float(input('Insira o terceiro número'))
maior = 0;
menor = 0;
if(num1>num2 and num2>num3):
	maior = num1
if(num1>num2 and num1>num3):
	maior = num1
if(num1<num2 and num2>num3):
	maior = num2
if(num1<num2 and num2<num3):
	maior = num3

if(num1<num2 and num2<num3):
	menor = num1
if(num1<num2 and num1<num3):
	menor = num1
if(num1>num2 and num2<num3):
	menor = num2
if(num1>num2 and num2>num3):
	menor = num3

print('O maior numero foi', maior)
print('O menor numero foi', menor)