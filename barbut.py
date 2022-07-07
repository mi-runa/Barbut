from random import randint
from time import sleep


# Progress bar
def zartimp():
    for i in range(101):
        sleep(0.01)
        print(f"\rSe rotesc zarurile  {i}%", end="", flush=True)
    print('\n')


def da_cu_zaru(text):
    logo_zar = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

    # Zaruri si logouri zaruri
    sarezaru1 = randint(1, 6)
    sarezaru2 = randint(1, 6)
    logozar1 = logo_zar[sarezaru1 - 1]
    logozar2 = logo_zar[sarezaru2 - 1]

    # Rezultat
    suma_zaruri = sarezaru1 + sarezaru2
    print(f"{text} {logozar1} + {logozar2}   {suma_zaruri}\n")
    return suma_zaruri


while True:
    # Evitare eroare daca baga litere
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

    # Timp de asteptare
    zartimp()

    # Se da cu zarul
    sum_jucator = da_cu_zaru("Ai dat:")
    sum_calculator = da_cu_zaru("Calculatoru a dat:")

    # Alegere castigator
    if sum_jucator == sum_calculator:
        print("Egalitate mai da o data\n")
    elif optiune == 1 and sum_jucator < sum_calculator or optiune == 2 and sum_jucator > sum_calculator:
        print("Ai castigat.\n")
    else:
        print("Te-a facut calculatoru. N-ai talent la zaruri.\n")

    # Inca o tura/oprire joc
    inca = input("Hai mai dam o data! (hai/orice alt raspuns): ")
    if inca != 'hai':
        print("Am inchis. Hai cu pacanelele 🂧🂧🂧")
        break
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
