a = str(input())
if a == "vertebrado":
    b = str(input())
    if b == "ave":
        c = str(input())
        if c == "carnivoro":
            print("aguia")
        elif c == "onivoro":
            print("pomba")    
    elif b == "mamifero":
        c = str(input())
        if c == "onivoro":
            print("homem")
        elif c == "herbivoro":
            print("vaca")
elif a == "invertebrado":
    b = str(input())
    if b == "inseto":
        c = str(input())
        if c == "hematofago":
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")
    elif b == "anelideo":
        c = str(input())
        if c == "hematofago":
            print("sanguessuga")
        elif c == "onivoro":
            print("minhoca")