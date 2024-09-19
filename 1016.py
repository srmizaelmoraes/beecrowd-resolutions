distancia = int(input())
carroy = int(90)
carrox = int(60)
diferencaVelocidade = (carroy - carrox)
afastamento = diferencaVelocidade / 60
tempo = int(distancia / afastamento)
print('{} minutos'.format(tempo))