hi, mi, hf, mf = map(int, input().split())

if hi == hf and mi == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

elif hf > hi:
    tempo = hf - hi

    if mi >= 60:
        tempo = tempo + 1
        print("")