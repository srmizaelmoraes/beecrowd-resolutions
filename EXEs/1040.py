n1, n2, n3, n4 = map(float, input().split())
m2, m3, m4, m1 = 2, 3, 4, 1
sumM = sum([m2, m3, m4, m1])
media = ((n1 * m2) + (n2 * m3) + (n3 * m4) + (n4 * m1)) / sumM
if media < 5:
    print("Media: {:.1f}\nAluno reprovado.".format(media))
elif media >= 5 and media <= 6.9:
    print("Media: {:.1f}\nAluno em exame.".format(media))
    notaExame = float(input())
    print("Nota do exame: {:.1f}".format(notaExame))
    novaMedia = (media + notaExame) / 2
    if novaMedia >= 5:
        print("Aluno aprovado.\nMedia final: {:.1f}".format(novaMedia))
    else:
        print("Aluno reprovado.\nMedia final: {:.1f}".format(novaMedia))
else:
    print("Media: {:.1f}\nAluno aprovado.".format(media))