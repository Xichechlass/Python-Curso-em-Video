print('Detector de palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
fraseinversa = str('')
tamanho = -len(frase)
for letra in range(-1, tamanho - 1, -1):
    fraseinversa += frase[letra]
print(f'O inverso de {frase} é {fraseinversa}')
if fraseinversa == frase:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
