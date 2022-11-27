def tiket_machine():
        def cosmotics():
                n1 = 1
                n2 = 0
                while True:
                    yield n1
                    n1,n2 = n1 + 1, n2 + 1
        Z = cosmotics()


        def perfumery():
            n1 = 1
            n2 = 0
            while True:
                yield n1
                n1, n2 = n1 + 1, n2 + 1


        Z2 = perfumery()


        def pharmaceutical():
            n1 = 1
            n2 = 0

            while True:
                yield n1
                n1, n2 = n1 + 1, n2 + 1


        Z3 = pharmaceutical()

        count = 1
        user_id = ["346260730", "341326205"]

        while count < 4:
            idnum = input("please  inter your id ")
            print('place try agn ', count)
            if idnum in user_id:
                while True:
                    ope = input("Enter your choice among the above option")
                    if ope == 'c':
                        print("Your ticket number is :",ope,"_", next(Z))
                    elif ope == 'p':
                        print("Your ticket number is :",ope,"_", next(Z2))

                    elif ope == 'ph':
                        print("Your ticket number is :",ope,"_", next(Z3))

            else:
                count += 1
                continue

        else:

            import time


        def countdown(t):
            while t:
                time.sleep(1)
                t -= 1


        countdown(int(5))
tiket_machine()
print("Thank you for coming you have finished your time:")
