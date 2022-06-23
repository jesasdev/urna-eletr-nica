# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


votoBolsonaro = 0
votoLula = 0
votoCiro = 0
votoBranco = 0
votoNulo = 0
votoTotal = 0
voto = 0
while voto > 0:
    voto = int(input('vote'))
    voto + 1
    if (voto == 22):
        votoBolsonaro += 1
        print('Bolsonaro')

    elif voto == 13:
        votoLula += 1
        print('Lula')

    elif voto == 12:
        votoCiro += 1
        print('Ciro')

    elif voto == 0:
        votoBranco += 1
        print('Voto branco')

    elif voto != 0 or voto != 12 or voto != 22 or voto != 13:
        votoNulo += 1
        print('Nulo')

    elif voto == 0 or voto == 12 or voto == 22 or voto == 13:
        votoTotal += 1
        print('Total')

voto = int(input())
print('Resultado')
print('total = ', votoTotal, '100%')

percentBolsonaro = float(100 * votoBolsonaro) / votoTotal
print('Bolsonaro = ', percentBolsonaro, '%')
percentLula = float(100 * votoLula) / votoTotal
print('Lula = ', percentLula, '%')
percentCiro = float(100 * votoCiro) / votoTotal
print('Ciro = ', percentCiro, '%')
percentBranco = float(100 * votoBranco) / votoTotal
print('Branco = ', percentBranco, '%')
percentNulo = float(100 * votoNulo) / votoTotal
print('Nulo = ', percentNulo, '%')

print('Voto Total = ', votoTotal, '%')
