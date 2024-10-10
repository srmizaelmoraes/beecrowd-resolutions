listPreco = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}
c, q = map(int, input().split())
if c in listPreco:
    total = q * listPreco[c]
    print("Total: R$ {:.2f}".format(total))