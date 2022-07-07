from random import randint
from time import sleep


def da_cu_zaru(text, logo_zar):
    # "Animatie"
    for i in range(randint(7, 21)):
        print(f"\r{logo_zar[randint(0, 5)]} {logo_zar[randint(0, 5)]}", end="", flush=True)
        sleep(0.2)

    # Zaruri finale
    sarezaru1 = randint(1, 6)
    sarezaru2 = randint(1, 6)

    # Rezultat
    suma_zaruri = sarezaru1 + sarezaru2
    print(f"\r{logo_zar[sarezaru1 - 1]} {logo_zar[sarezaru2 - 1]}")
    print(f"{text} {suma_zaruri}")
    sleep(0.7)
    return suma_zaruri


# Lista cu logo-uri
lista_logo_zar = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

while True:
    # Evitare eroare daca nu baga cifre
    try:
        optiune = int(input("⚀ La mai mica - apasa 1\n⚅ La mai mare - apasa 2\n  Iesi - apasa 0\nAlege: "))
    except ValueError:
        print("Alege o cifra bo$$!\n")
        continue

    # Alegere joc
    if optiune == 0:
        print("Am inchis. Hai cu pacanelele 🂧🂧🂧")
        break
    elif optiune == 1:
        print("La mai mica")
    elif optiune == 2:
        print("La mai mare")
    else:
        print(f"{optiune} nu e o optiune.\n")
        continue

    # Se da cu zarul
    sum_jucator = da_cu_zaru("Ai dat:", lista_logo_zar)
    sum_calculator = da_cu_zaru("Calculatoru a dat:", lista_logo_zar)

    # Alegere castigator
    if sum_jucator == sum_calculator:
        print("Egalitate mai da o data")
    elif optiune == 1 and sum_jucator < sum_calculator or optiune == 2 and sum_jucator > sum_calculator:
        print("Ai castigat.")
    else:
        print("Te-a facut calculatoru. N-ai talent la zaruri.")

    # Inca o tura/ oprire joc
    inca = input("Hai mai dam o data! (hai/orice alt raspuns): ")
    if inca != 'hai':
        print("Am inchis. Hai cu pacanelele 🂧🂧🂧")
        break
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
