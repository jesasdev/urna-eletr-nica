
print('Vote')
voto = 0
votoTotal = 0
votoBolsonaro =0
votoLula=0
votoCiro =0
votoBranco = 0
votoNulo =0
while voto >=0:
    voto = int(input())
    if voto<0:
        break
    elif voto == 22:
        votoBolsonaro= votoBolsonaro+1
        print('Bolsonaro')
    elif voto == 13:
        votoLula=votoLula+1
        print('Lula')
    elif voto == 12:
        votoCiro =votoCiro+1
        print('Ciro')
    elif voto ==0:
        votoBranco =votoBranco+1
        print('Branco')
    elif voto !=22 or voto!= 13 or voto != 12 or voto != 0 :
        votoNulo = votoNulo+1
        print('Nulo')

else:

   print('Fim')

votoTotal = votoBolsonaro + votoLula+votoBranco+votoNulo+votoCiro
primeiroTurno = (votoBolsonaro+votoLula+votoCiro)/2
percentLula = float(100*votoLula)/votoTotal
percentBolsonaro = float(100*votoBolsonaro)/votoTotal
percentCiro = float(100*votoCiro)/votoTotal
percentBranco = float(100*votoBranco)/votoTotal
percentNulo = float(100*votoNulo)/votoTotal

print('Bolsonaro',votoBolsonaro,percentBolsonaro.__format__('.2f'),'%')
print('Lula',votoLula,percentLula.__format__('.2f'),'%')
print('Ciro',votoCiro,percentCiro.__format__('.2f'),'%')
print('Branco',votoBranco,percentBranco.__format__('.2f'),'%')
print('Nulo',votoNulo,percentNulo.__format__('.2f'),'%')
print('Votos Total',votoTotal,'100%')

if(votoBolsonaro>=primeiroTurno):
    print('Bolsonaro Eleito com ',percentBolsonaro.__format__('.2f'),'% dos votos válidos','\nTotal de votos:',votoBolsonaro)
elif votoLula>=primeiroTurno:
    print('Lula Eleito com ',votoLula,' votos:',percentLula.__format__('.2f'),'%')
elif votoCiro>=primeiroTurno:
    print('Ciro Eleito com',votoCiro,' votos:',percentCiro.__format__('.2f'),'%')
else:
    print('Com os resultados:','\nBolsonaro:',percentBolsonaro.__format__('.2f'),'%',' \nLula:',percentLula.__format__('.2f'),'%',
          '\nCiro:',percentCiro.__format__('.2f'),'%','\nÉ necessário segundo Turno')