"""
Zadanie 1 - Weryfikacja numeru PESEL

Opis zadania:
- Użytkownik wprowadza numer PESEL (ciąg 11 znaków, zakładamy, że długość jest poprawna).
- Program sprawdza, czy ostatnia cyfra (cyfra kontrolna) jest prawidłowa.
- Reguła: znaleźć w internecie.
- Jeśli ostatnia cyfra zgadza się z obliczoną wartością, funkcja ma zwrócić 1, w przeciwnym wypadku 0.

Przykładowe wejście:
    "97082123152"
Przykładowe wyjście:
    0

Wymagania:
- Implementacja funkcji `verify_pesel(pesel: str) -> int`.
- Użycie algorytmu weryfikacji opisanej powyżej.

123

"""


def verify_pesel(pesel: str) -> int:
    control_num = 0
    numbers = []
    weight = [1,3,7,9,1,3,7,9,1,3,0]
    for char in pesel:
        numbers.append(int(char))
    for i in range(len(numbers)):
        control_num += weight[i] * numbers[i] % 10
    control_num = control_num % 10
    if control_num != 0:
        control_num = 10 - control_num
    if numbers[-1] == control_num:
        return 1
    else: return 0


# Przykładowe wywołanie:
if __name__ == "__main__":
    pesel_input = "97082123152"
    print(verify_pesel(pesel_input)) # Oczekiwane wyjście: 0
    print(verify_pesel("03272509730")) # Oczekiwane wyjście: 1
    print(verify_pesel("02070803628")) # Oczekiwane wyjście: 1
    print(verify_pesel("47738929293"))  # Oczekiwane wyjście: 0