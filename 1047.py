hi, mi, hf, mf = map(int, input().split())
if hi == hf and mi == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    miT = mf - mi
    if miT < 0:
        miT += 60
        hf -= 1
    hrT = hf - hi
    if hrT < 0:
        hrT += 24
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hrT, miT))