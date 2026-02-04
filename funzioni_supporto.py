from funzioni_services import inserisci_fattura, mostra_fatture

def menu():
    #permette di salvare le fatture dopo averne chiesto i campi da riempire
    print("1) Salva fattura")

    #mostra tutte le fatture nel db
    print("2) Mostra fatture")

    print("0) Termina")

def scelta():
    while True:
        menu()
        opzione = int(input("Scelta: "))

        if opzione == 1:
            inserisci_fattura()
        elif opzione == 2:
            mostra_fatture()
        elif opzione == 0:
            break