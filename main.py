# ZADANIE DOMOWE NR 1
# Napisz OBIEKTOWO mały sklep w Python.
# Użyj: obsługi wyjątków, zaprojektuj minimum 3 metody, sam backend
# obsługa przez terminal

from klasy import Sklep, Produkt, Koszyk
import os



def startTest():

    p1 = Produkt("Ogórek", 10, 5)
    p2 = Produkt("Banan", 15, 3)
    p3 = Produkt("Pomidor", 13, 6)

    lista_produktow = [p1, p2, p3]

    moj_sklep = Sklep("MOJ SKLEP", lista_produktow)

    print(moj_sklep)

    moj_sklep.pokaz_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if True:
        startTest()
    else:
        pass


