import random


class Klient:
    def __init__(self, imie, nazwisko, pesel, konto=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.konto = konto

    def display_data(self):
        print(f"Imie= {self.imie}\n"
              f"Nazwisko= {self.nazwisko}\n"
              f"Pesel= {self.pesel}")


class Bank:
    def __init__(self, nazwa, adres):
        self.nazwa_banku = nazwa
        self.adres_glowny = adres

    @staticmethod
    def Autoryzacja(numer_transakcji, status=True):
        if status:
            print("Autoryzacja transakcji " + str(numer_transakcji))
            return True
        print("Transakcja się nie powiodła")
        return False

class Konto:
    def __init__(self, srodki, rachunki=None):
        self.srodki = srodki
        self.rachunki = rachunki


class Rachunek(Konto):
    def __init__(self, srodki):
        super().__init__(srodki)
        self.type = ""
        self.oprocentowanie = None

    def dodajRachunekOszczednosciowy(self, oprocentowanie):
        self.type = "oszczędnościowy"
        self.oprocentowanie = oprocentowanie

    def dodajRachunekOsobisty(self):
        self.type = "osobisty"


class Transakcja:
    def __init__(self, konto):
        self.id = random.randint(0, 10000)
        self.konto = konto

    def wyplata(self):
        kwota = input("Podaj kwotę wypłatyz konta:")
        if self.konto.srodki < float(kwota):
            print("Transakcja odrzucona.")
            return None
        return kwota

    def wplata(self):
        kwota = input("Podaj kwotę wpłaty:")
        return kwota

    def przelew(self):
        kwota = input("Podaj kwotę przelwu:")
        nr_konta = input("Podaj numer konta na który ma zostać wykonany przelew:")
        if self.konto.srodki < float(kwota):
            print("Transakcja odrzucona.")
            kwota = None
        return kwota, nr_konta

    def sprawdzStanKonta(self):
        return self.konto.srodki

    def wnioskujOkredyt(self):
        kwota = input("Podaj kwotę kredytu:")
        lata = input("Podaj ilość lat do spłaty kredytu:")
        print(f"Wniosek kredytowy\nWysokość kwoty: {kwota}\nlata: {lata}")
        return kwota, lata


class Pracownik:
    def __init__(self, imie_pracownika, nazwisko_prcownika):
        self.imie_pracownika = imie_pracownika
        self.nazwisko_pracownika = nazwisko_prcownika

    def weryfikacjaDanych(self, klient, data):
        if klient.imie != data["imie"] or klient.nazwisko != data["nazwisko"]:
            print("Niepoprawne imie lub nazwisko.")
            return False
        if klient.pesel != data["pesel"]:
            print("Niepopawny pesel.")
            return False
        if not self.sprawdz_w_bazie(data["dlugi"]) or \
                not self.sprawdz_w_bazie(data["dochod"]):
            return False
        return True

    def analizaZdolnosciKredytowej(self, klient, kwota_kredytu, lata):
        data = self.podaj_dane_podane_przez_klienta()
        if not self.weryfikacjaDanych(klient, data):
            return False

        if float(kwota_kredytu) > float(lata) * float(data["dochod"]):
            return False
        if data["dlugi"] == "TAK":
            return False
        return True

    def utworzRachunekBankowy(self, klient, srodki, oszczednosciowy = True, oprocentowanie = None):
        data = self.podaj_dane_podane_przez_klienta()
        if not self.weryfikacjaDanych(klient, data):
            return False
        if oszczednosciowy:
            rachunek = Rachunek(srodki).dodajRachunekOszczednosciowy(oprocentowanie)
        else:
            rachunek = Rachunek(srodki).dodajRachunekOsobisty()
        klient.konto.rachunki.append(rachunek)

    @staticmethod
    def sprawdz_w_bazie(data):
        return True

    @staticmethod
    def podaj_dane_podane_przez_klienta():
        imie = input("Podaj imie:")
        nazwisko = input("Podaj nazwisko:")
        pesel = input("Podaj numer pesel:")
        dochod = input("Podaj dochód roczny:")
        dlugi = input("Czy klient ma zaległości w spłątach kredytów? (TAK/NIE)")
        data = {
            "imie": imie,
            "nazwisko": nazwisko,
            "pesel": pesel,
            "dochod": dochod,
            "dlugi": dlugi.upper()
        }
        return data


def main():
    mbank = Bank("Mbank", "")
    konto01 = Konto(5000.00)
    klient1 = Klient("Agata", "Niewiadomska", "00022211144", konto01)
    klient1.display_data()
    pracownik01 = Pracownik("Aneta", "Bolek")
    opcja = input("Wybierz transakcję:\n"
                   "1.Wniosek o kredyt\n"
                   "2.Przelew\n"
                  "3. Wpłata\n"
                  "4. Wypłata\n"
                  "5. Sprawdź stan konta\n")
    t1 = Transakcja(konto01)
    if opcja == "1":
        kwota, lata= t1.wnioskujOkredyt()
        stat = pracownik01.analizaZdolnosciKredytowej(klient1, kwota, lata)
        mbank.Autoryzacja(t1.id, stat)
    elif opcja == "2":
        kwota, nr_konta = t1.przelew()
        stat = True
        if not kwota:
            stat = False
        mbank.Autoryzacja(t1.id, stat)
    elif opcja == "3":
        kwota = t1.wplata()
        stat = True
        mbank.Autoryzacja(t1.id, stat)
        print(f"Wpłata {kwota} na konto")
    elif opcja == "4":
        kwota = t1.wyplata()
        stat = True
        if not kwota:
            stat = False
        mbank.Autoryzacja(t1.id, stat)
    elif opcja == "5":
        srodki = t1.sprawdzStanKonta()
        mbank.Autoryzacja(t1.id, True)
        print(f"Srodki na koncie: {srodki}")


if __name__ == "__main__":
    main()

