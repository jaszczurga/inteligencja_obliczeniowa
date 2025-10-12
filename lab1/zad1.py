from datetime import datetime
import math

def oblicz_fale_fizyczna(dzien_zycia):
    return math.sin((2 * math.pi * dzien_zycia)/23)

def oblicz_fale_emocjonalna(dzien_zycia):
    return math.sin((2 * math.pi * dzien_zycia)/28)

def oblicz_fale_intelektualna(dzien_zycia):
    return math.sin((2 * math.pi * dzien_zycia)/33)

imie = input("Podaj swoje imię: ")
rok_urodzenia = int(input("Podaj swój rok urodzenia: "))
miesiac_urodzenia = int(input("Podaj swój miesiąc urodzenia (1-12): "))
dzien_urodzenia = int(input("Podaj swój dzień urodzenia (1-31): "))

data_urodzenia = datetime(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)
dzien_zycia = (datetime.now() - data_urodzenia).days
print(f"{imie}, żyjesz już {dzien_zycia} dni.")

fizyczna_fala = oblicz_fale_fizyczna(dzien_zycia)
fala_emocjonalna = oblicz_fale_emocjonalna(dzien_zycia)
fala_intelektualna = oblicz_fale_intelektualna(dzien_zycia)


print(f"Twoja fizyczna fala: {fizyczna_fala:.2f}")
print(f"Twoja emocjonalna fala: {fala_emocjonalna:.2f}")
print(f"Twoja intelektualna fala: {fala_intelektualna:.2f}")


GOOD_RESULT_THRESHOLD = 0.5
BAD_RESULT_THRESHOLD = -0.5

if fizyczna_fala > GOOD_RESULT_THRESHOLD:
    print("Twoja kondycja fizyczna jest bardzo dobra.")
elif fizyczna_fala < BAD_RESULT_THRESHOLD:
    print("Twoja kondycja fizyczna jest słaba.")
    if oblicz_fale_fizyczna(dzien_zycia + 1) > GOOD_RESULT_THRESHOLD:
        print("Jutro będzie lepiej!")

if fala_emocjonalna > GOOD_RESULT_THRESHOLD:
    print("Twoje samopoczucie jest bardzo dobre.")
elif fala_emocjonalna < BAD_RESULT_THRESHOLD:
    print("Twoje samopoczucie jest słabe.")
    if oblicz_fale_emocjonalna(dzien_zycia + 1) > GOOD_RESULT_THRESHOLD:
        print("Jutro będzie lepiej!")

if fala_intelektualna > GOOD_RESULT_THRESHOLD:
    print("Twoja zdolność koncentracji jest bardzo dobra.")
elif fala_intelektualna < BAD_RESULT_THRESHOLD:
    print("Twoja zdolność koncentracji jest słaba.")
    if oblicz_fale_intelektualna(dzien_zycia + 1) > GOOD_RESULT_THRESHOLD:
        print("Jutro będzie lepiej!")

