def perfumery_number():
    n1 = 1
    n2 = 0
    while True:
        yield n1
        n1, n2 = n1 + 1, n2 + 1

