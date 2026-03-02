# 1. Bezpieczny kalkulator: Napisz program, który w pętli prosi użytkownika o podanie dwóch
# liczb i operacji ( + , - , * , / ). Zaimplementuj pełną obsługę błędów ValueError (gdy
# dane nie są liczbami) i ZeroDivisionError . Dodaj blok else do wyświetlania wyniku i
# finally z komunikatem "Kolejna operacja...".

def task_1():
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
            print(f"{e}")
        else:
            print(f"{number_1} {operation} {number_2} = {result}")
        finally:
            print("Kolejna operacja...")



# 2. Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym, zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż 18. Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek.

class WiekNiepoprawnyError(Exception):
    pass

def task_2():
    def rejestruj_uzytkownika(wiek):
        if wiek < 18:
            raise WiekNiepoprawnyError

    try:
        rejestruj_uzytkownika(15)
    except WiekNiepoprawnyError:
        print(f"Użytkownik musi mieć conajmniej 18 lat")

# 3. Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
# Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie
# ma uprawnień do odczytu).

def task_3():
    filename = "C:/Users/grazy/Desktop/python_lessons/lesson_8/data.txt"

    def read_file(filename):
        try:
            file = open(filename)
            print(f"File: {file}")
        except FileNotFoundError as e:
            print(f"Plik nie istnieje: {e}")
        except PermissionError as e:
            print(f"Brak dostępu do pliku: {e}")

    read_file(filename)


# 4. Asercja w funkcji: Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z
# listy. Użyj assert , aby upewnić się, że przekazana lista nie jest pusta.

def task_4():
    def oblicz_srednia(lista_ocen):      
        assert 0 < len(lista_ocen), "Lista nie może być pusta" 
        return sum(lista_ocen)/len(lista_ocen)
    
    oblicz_srednia([])

# 5. Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego
# treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku
# finally , aby upewnić się, że plik z logami jest zawsze zamykany.

def task_5():
    filename = "C:/Users/grazy/Desktop/python_lessons/lesson_8/data.txt"
    try:
        file = open(filename, mode='a')
    except FileNotFoundError as e:
        print(f"Plik nie istnieje: {e}")
    except PermissionError as e:
        print(f"Brak dostępu do pliku: {e}")

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
        print(f"{e}")
        file.write(f"\n{e}")
    else:
        print(f"{number_1} {operation} {number_2} = {result}")
    finally:
        print("Kolejna operacja...")
        file.close()

# 6. Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , która w bloku
# try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w
# słowniku), loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek
# BladPrzetwarzaniaDanychError z informacją, którego klucza brakowało.

class BladPrzetwarzaniaDanychError(Exception):
    pass

def task_6():
    dictionary = {
            "key_1": 2,
            "key_2": 3
    }

    def przetworz_dane(dane):        
        try:
            print(dane["key_3"])
        except KeyError as e:
            print(f"Nie ma takiego klucza w słowniku! {e}")
            raise BladPrzetwarzaniaDanychError(f"Brakuje klucza: {e}")
        
    przetworz_dane(dictionary)

# 7. Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik,
# klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
# nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except
# (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except
# KeyError .

def task_7():
    # def pobierz_wartosc(slownik, klucz):
    #     return slownik.get(klucz, None)

    def pobierz_wartosc(slownik, klucz):
        try:
            return slownik[klucz]
        except KeyError as e:
            print(f"Nie ma takiego klucza w słowniku! {e}")

    slownik = {
            "key_1": 2,
            "key_2": 3
    }
    
    pobierz_wartosc(slownik, "key_3")


# 8. Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę
# wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym
# problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError ,
# przekazując do niego tę listę.

class BladWalidacjiError(Exception):
    pass

def task_8():
    def validate_password(password):
        errors_list = []
        if len(password.strip()) < 8:
            errors_list.append("Hasło jest za krótkie")
        
        if not any(char.isdigit() for char in password):
            errors_list.append("Hasło nie zawiera cyfry!")

        if not any(char.isupper() for char in password):
            errors_list.append("Hasło nie zawiera dużej litery!")

        if not any(not char.isalnum() and not char.isspace() for char in password):
            errors_list.append("Hasło nie zawiera znaku specjalnego!")

        if errors_list:
            raise BladWalidacjiError(errors_list)
        return errors_list
    
    validate_password("hAslokk3*")

# 9. Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
# kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
# pliku.

def task_9():
    filename = "C:/Users/grazy/Desktop/python_lessons/lesson_8/data.txt"

    def read_file(filename):
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                content = f.read()
                print(content)

        except FileNotFoundError:
            print("Plik nie istnieje")

        except PermissionError:
            print("Brak uprawnień do pliku")

        except Exception as e:
            print(f"Wystąpił inny nieoczekiwany błąd: {e}")

    read_file(filename)

# 10. Mini-projekt: Sumator liczb z pliku: Napisz program, który:
# a. Pyta użytkownika o nazwę pliku.
# b. Otwiera plik i czyta go linia po linii.
# c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
# d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
# e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
# f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po
# drodze).

def task_10():
    filename = input("Podaj nazwę pliku: ")
    total = 0.0

    try:
        with open(filename, mode="r", encoding="utf-8") as f:
            for line in f:
                try:
                    total += float(line.strip())
                except ValueError:
                    pass

        print(f"Suma wynosi: {total}")

    except FileNotFoundError:
        print("Plik nie istnieje")

    except PermissionError:
        print("Brak uprawnień do pliku")

    except Exception as e:
        print(f"Wystąpił inny nieoczekiwany błąd: {e}")


task_10()
