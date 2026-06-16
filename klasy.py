from procedury import clear_screen, daj_prompt_z_zakresu_liczb

class Koszyk:
    def __init__(self):
        self.zawartosc = []

    def __str__(self):
        return "Zawartość koszyka: " + str(self.zawartosc)

    def dodaj_produkt(self, produkt, ilosc):
        if produkt.ilosc >= ilosc:
            produkt.ilosc = produkt.ilosc - ilosc

            self.zawartosc.append((produkt, ilosc))

        else:
            print("Więcej chcesz niż jest")

    def wyswietl(self):
        print("Zawartość koszyka:")
        if len(self.zawartosc) == 0:
            print("Koszyk jest pusty")
        else:
            for produkt, ilosc in self.zawartosc:
                print(f"{produkt.nazwa} - cena({produkt.cena}) - ilosc({ilosc})")

class Produkt:
    def __init__(self, nazwa, cena, ilosc):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc = ilosc

    def __str__(self):
        return f"--{self.nazwa}-- cena:{self.cena} ilosc:{self.ilosc}"

    def __repr__(self):
        return f"--{self.nazwa}-- cena:{self.cena} ilosc:{self.ilosc}"

class Sklep:
    def __init__(self, nazwa, lista_produktow):
        self.nazwa = nazwa
        self.lista_produktow = lista_produktow
        self.koszyk = Koszyk()

    def __str__(self):
        return f"Name: {self.nazwa}\nListOfProducts: {self.lista_produktow}\n"

#    def __repr__(self):
        return f"Name: {self.name}\nListOfProducts: {self.listOfProducts}\n"
    def pokaz_menu(self):

        while True:
            print(f"------------- {self.nazwa} -------------")
            print("         1. Pokaż produkty")
            print("         2. Dodaj do koszyka")
            print("         3. Pokaż koszyk")
            print("         4. Wyjdź ze sklepu")

            menu = daj_prompt_z_zakresu_liczb("Wybierz opcję:", 1, 4)
            clear_screen()
            if menu == 1:
                print("    --- Lista produktów ---")
                for index, produkt in enumerate(self.lista_produktow):
                    print(f"    {index+1}:{self.lista_produktow[index]}")
            elif menu == 2:
                self.dodaj_do_koszyka()
            elif menu == 3:
                self.koszyk.wyswietl()
            elif menu == 4:
                return

    def dodaj_do_koszyka(self):

        def dodaj_do_koszyka_produkt(produkt, koszyk):
            clear_screen()
            if produkt.ilosc == 0:
                print(f"Produkt: {produkt.nazwa} jest chwilowo niedostępny")
            else:
                while True:
                    print(f"Wybrałeś produkt: {produkt}")
                    ilosc_produktu = daj_prompt_z_zakresu_liczb(f"Podaj ilość produktu ({0}-{produkt.ilosc})(0-wyjście): {produkt.nazwa}", 0, produkt.ilosc)
                    if ilosc_produktu == 0:
                        return
                    elif 0 < ilosc_produktu <= produkt.ilosc:
                        koszyk.dodaj_produkt(produkt, ilosc_produktu)
                        clear_screen()
                        koszyk.wyswietl()
                        return
                    else:
                        print(f"Nie ma tyle ilości produktu {produkt.nazwa}. Jest sztuk {produkt.ilosc}")

        while True:

            print("\n------------- LISTA PRODUKTÓW -------------")
            for index, produkt in enumerate(self.lista_produktow):
                print(      f"{index+1}. {produkt}")
            print(f"{len(self.lista_produktow)+1}. Wyjście do głównego Menu")

            menu_koszyk = daj_prompt_z_zakresu_liczb("Podaj co chcesz włożyć do koszyka", 1, len(self.lista_produktow)+1)
            if menu_koszyk in [x for x in range(1, len(self.lista_produktow)+1)]:
                produkt = self.lista_produktow[menu_koszyk-1]
                dodaj_do_koszyka_produkt(produkt, self.koszyk)

            elif menu_koszyk == len(self.lista_produktow)+1:
                clear_screen()
                break