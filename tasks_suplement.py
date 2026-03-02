# Ćwiczenie S1: Bezpieczna konwersja
# Napisz funkcję bezpieczny_int(tekst) zwracającą liczbę całkowitą lub None, jeśli konwersja się
# nie uda. Użyj try/except ValueError.
# Wskazówka: try: return int(tekst) / except ValueError: return None.

def task_1():
    def bezpieczny_int(tekst):
        try:
            return int(tekst)
        except ValueError:
            return None
        

    print(bezpieczny_int("tekst"))
    print(bezpieczny_int(10))

# Ćwiczenie S2: Bezpieczne dzielenie
# Napisz funkcję podziel(a, b) zwracającą wynik dzielenia. Jeśli b == 0, zamiast błędu zwróć tekst
# "Nie można dzielić przez zero". Użyj try/except ZeroDivisionError.
# Wskazówka: try: return a / b / except ZeroDivisionError: return "Nie można dzielić przez zero".

def task_2():
    def podziel(a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Nie można dzielić przez 0"
        
    print(podziel(12,4))
    print(podziel(5,0))

# Ćwiczenie S3: Bezpieczny dostęp do listy
# Napisz funkcję pobierz_element(lista, indeks) zwracającą element o podanym indeksie. Jeśli
# indeks jest poza zakresem, zwróć None. Użyj try/except IndexError.
# Wskazówka: try: return lista\[indeks\] / except IndexError: return None

def task_3():
    def pobierz_element(lista, indeks):
        try:
            return lista[indeks]        
        except IndexError:
            return None
        
    print(pobierz_element([1,2,3], 1))
    print(pobierz_element([1,2,3], 3))
        
# Ćwiczenie S4: Pobieranie liczby z walidacją
# Napisz funkcję pobierz_liczbe_z_zakresu(minimum, maksimum) która w pętli prosi o liczbę. Jeśli
# nie jest liczbą — ValueError. Jeśli poza zakresem — wyświetl komunikat i pytaj ponownie. Użyj
# else do potwierdzenia sukcesu.
# Wskazówka: while True + try/except ValueError + if/else do sprawdzenia zakresu.

def task_4():
    def pobierz_liczbe_z_zakresu(minimum, maksimum):
        while True:
            try:
                number = int(input(f"Podaj liczbę z zakresu od {minimum} do {maksimum}"))

            except ValueError:
                return "To nie jest liczba!"
            
            if minimum <= number <= maksimum:
                print(f"Super! Podałeś liczbę {number}, która jest z podanego zakresu.")
            else:
                print("Podana liczba jest poza zakresem!")

    print(pobierz_liczbe_z_zakresu(5,10))

# Ćwiczenie S5: Własny wyjątek z kontekstem
# Zdefiniuj wyjątek TemperaturaKrytycznaError przechowujący temperaturę i limit. Napisz funkcję
# sprawdz_temperature(temp, limit=100), która rzuca ten wyjątek gdy temp > limit.
# Wskazówka: class TemperaturaKrytycznaError(Exception): def __init__(self, temp, limit): ...
class TemperaturaKrytycznaError(Exception): 
    def __init__(self, temp, limit):
        self.alert = f"Podana temperatura: {temp} jest za wysoka! Limit to: {limit}"
        super().__init__(self.alert)

def task_5():
    def sprawdz_temperature(temp, limit=100):
        try:
            if temp > limit:
                raise TemperaturaKrytycznaError(temp, limit)
        except TemperaturaKrytycznaError as e:
            print(f"Błąd: {e.alert}")
        
    sprawdz_temperature(150)

# Ćwiczenie S6: Logowanie do pliku
# Napisz funkcję zaloguj_blad(komunikat, plik="log.txt") która dopisuje komunikat do pliku. Użyj
# trybu "a" i with open(). Przetestuj, wywołując ją kilka razy.
# Wskazówka: with open(plik, "a") as f: f.write(komunikat + "\\n").

def task_6():
    def zaloguj_blad(komunikat, plik="log.txt"):
        with open(plik, "a") as f:
            f.write(komunikat + "\n")

    zaloguj_blad("dopisuje linie")

# Ćwiczenie S7: Kalkulator z logowaniem
# Napisz kalkulator (zadanie 1), ale każdy błąd loguj do pliku "kalkulator_log.txt" zamiast
# wyświetlać. Użyj funkcji z ćwiczenia S6.
# Wskazówka: W except: zaloguj_blad(str(e)).

def task_7():
    def zaloguj_blad(komunikat, plik="log.txt"):
        with open(plik, "a") as f:
            f.write(komunikat + "\n")

    while(True):
        try:
            number_1 = float(input("Podaj pierwszą liczbę: "))
            number_2 = float(input("Podaj drugą liczbę: "))
            operation = input("Podaj operacje +,-,*,/ : ")

            if operation == '+':
                result = number_1 + number_2
            elif operation == '-':
                result = number_1 - number_2
            elif operation == '*':
                result = number_1 * number_2
            elif operation =='/':
                result = number_1 / number_2
            else:
                print("Nieprawidłowa operacja!")
        except (ValueError, ZeroDivisionError) as e:
            zaloguj_blad(f"{e}", "kalkulator_log.txt")
            print(f"{e}")
        else:
            print(f"{number_1} {operation} {number_2} = {result}")
        finally:
            print("Kolejna operacja...")

# Ćwiczenie S8: Walidator formularza
# Napisz funkcję waliduj_formularz(dane) przyjmującą słownik. Zbierz błędy do listy:
# Brak klucza "imie" lub puste imie -- blad
# Brak klucza "email" lub brak "@" w emailu -- blad
# Brak klucza "wiek" lub wiek < 0 -- blad
# Jeśli są błędy, rzuć BladWalidacjiError(bledy). Użyj .get() do bezpiecznego dostępu.
# Wskazówka: Użyj dane.get("imie", "") do pobrania wartości domyślnej. Sprawdzaj każdy
# warunek i dodawaj do listy bledy.

class BladWalidacjiError(Exception):
    def __init__(self, errors):
        self.alert = errors
        super().__init__(self.alert)

def task_8():
    def waliduj_formularz(dane):
        errors = []
        if dane.get("imie", "") == "":
            errors.append("Nie podano pola imie!")
        if dane.get("email", "") == "":
            errors.append("Nie podano pola email!")
        elif "@" not in dane.get("email", ""):
            errors.append("Podany email jest nieprawidłowy!")
        if dane.get("wiek", "") == "":
            errors.append("Nie podano pola wiek!")
        elif not str(dane.get("wiek", "")).isdigit():
            errors.append("Podany wiek nie jest liczbą!")
        elif dane.get("wiek", "") < 0:
            errors.append("Podany wiek jest mniejszy od zera!")

        try:
            if errors:
                raise BladWalidacjiError(errors)
        except BladWalidacjiError as e:
            print(f"Błędy: {e.alert}")

    form_data = {
        "imie": "",
        "email": "maill",
        "wiek": ""
    }

    waliduj_formularz(form_data)

# Ćwiczenie S9: Retry z limitem prób
# Napisz funkcję wykonaj_z_retry(funkcja, max_prob=3) która wywołuje podaną funkcję. Jeśli rzuci
# wyjątek — próbuje ponownie, maksymalnie max_prob razy. Jeśli wszystkie próby się nie powiodą
# — rzuca ostatni wyjątek.
# Wskazówka: Pętla for i in range(max_prob): try/except. W except: zapisz wyjątek. Po pętli: raise
# ostatni_wyjatek.

def task_9():

    def funkcja():
        number_1 = int(input("Podaj pierwszą liczbę: "))
        number_2 = int(input("Podaj drugą liczbę: "))
        return number_1 / number_2

    def wykonaj_z_retry(funkcja, max_prob=3):
        print(f"Masz {max_prob} prób na wykonanie funkcji")
        ostatni_wyjatek = None

        for i in range(max_prob):
            try:
                wynik = funkcja()
                print("Funkcja wykonana pomyślnie")
                return wynik
            except Exception as e:
                print(f"Błąd! {e}")
                ostatni_wyjatek = e
                
        raise ostatni_wyjatek

    try:
        wynik = wykonaj_z_retry(funkcja, 3)
        print(f"Wynik: {wynik}")
    except Exception as e:
        print(f"Nie udało się wykonać funkcji. Ostatni błąd: {e}")  

# Ćwiczenie S10: Mini-projekt: Menedżer kontaktów
# Napisz program przechowujący kontakty w słowniku. Funkcje:
# dodaj_kontakt(kontakty, imie, telefon) — dodaje kontakt, raise ValueError jeśli imie jest
# puste
# pobierz_kontakt(kontakty, imie) — zwraca telefon lub raise KeyError
# usun_kontakt(kontakty, imie) — usuwa kontakt lub raise KeyError
# Główna pętla: menu z opcjami (dodaj, pobierz, usuń, wyjdź). Każda operacja w try/except.
# Zapisz kontakty do pliku "kontakty.txt" w finally na końcu programu.
# Wskazówka: Słownik kontakty = {}. W pętli while True: wyświetl menu, pobierz wybór, wywołaj
# odpowiednią funkcję w try/except.

def task_10():
    contacts = {}

    def dodaj_kontakt(kontakty, imie, telefon):
        if not imie:
            raise ValueError("Imię nie może być puste")
        elif imie in kontakty:
            raise ValueError("Kontakt o takim imieniu już istnieje")
        else:
            kontakty[imie] = telefon
            print("Wszystkie kontakty po dodaniu:")
            for i, t in kontakty.items():
                print(f"{i} : tel. {t}") 

    def pobierz_kontakt(kontakty, imie):
        if imie not in kontakty:
            raise KeyError("Nie ma kontaktu z takim imieniem!")
        else:
            tel = kontakty.get(imie)
            print(f"Nr tel kontaktu {imie} to {tel}")
            return tel

    def usun_kontakt(kontakty, imie):
        if imie not in kontakty:
            raise KeyError("Nie ma kontaktu z takim imieniem do usunięcia!")
        else:
            del kontakty[imie]
            print("Wszystkie kontakty po usunieciu:")
            for i, t in kontakty.items():
                print(f"{i} : tel. {t}") 

    def main():
        while True:
            try:
                choice = int(input("1-Dodaj 2-Pobierz 3-Usuń 4-Pokaż 5-Wyjście: "))
            except ValueError:
                print("Podaj liczbę 1–5")
                continue

            try:
                if choice == 1:
                    firstname = input("Podaj imię: ").strip()
                    phone = input("Podaj nr tel: ").strip()
                    dodaj_kontakt(contacts, firstname, phone)

                elif choice == 2:
                    firstname = input("Podaj imię: ").strip()
                    pobierz_kontakt(contacts, firstname)

                elif choice == 3:
                    firstname = input("Podaj imię: ").strip()
                    usun_kontakt(contacts, firstname)

                elif choice == 4:
                    if not contacts:
                        print("Brak kontaktów")
                    else:
                        for name, phone in contacts.items():
                            print(f"{name} : tel. {phone}")

                elif choice == 5:
                    print("Do zobaczenia!")
                    break

                else:
                    print("Wybierz liczbę 1,2,3,4 lub 5")

            except (ValueError, KeyError) as e:
                print(f"Błąd! {e}")

            finally:
                with open("contacts.txt", "w", encoding="utf-8") as f:
                    for name, phone in contacts.items():
                        f.write(f"{name},{phone}\n")

    main()        

task_10()