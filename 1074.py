i = 1
q = int(input())

while i <= q:
    i += 1
    n = int(input())

    if n == 0:
        print("NULL")
    else:
        if n > 0 and n % 2 == 0:
            print("EVEN POSITIVE")
        elif n < 0 and n % 2 == 1:
            print("ODD NEGATIVE")
        elif n > 0 and n % 2 == 1:
            print("ODD POSITIVE")
        else:
            print("EVEN NEGATIVE")