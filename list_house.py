from cosmetics import cosmotics_number
from perfume import perfumery_number
from pharmacy import pharmaceutical
from  timer import countdown

def tiket_machine():

    Z = cosmotics_number()
    Z2 = perfumery_number()
    Z3 = pharmaceutical()
    countdown(int(5))
    count = 1
    user_id = ["346260730", "341326205"]

    while count < 4:
        idnum = input("please  inter your id ")
        print('place try agn ', count)
        if idnum in user_id:
            while True:
                ope = input("Enter your choice among the above option")
                if ope == 'c':
                    print("Your ticket number is :", ope, "_", next(Z))
                elif ope == 'p':
                    print("Your ticket number is :", ope, "_", next(Z2))

                elif ope == 'ph':
                    print("Your ticket number is :", ope, "_", next(Z3))

        else:
            count += 1
            continue

    else:
        tiket_machine()
        print("Thank you for coming you have finished your time:")



