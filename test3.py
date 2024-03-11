import random

def nasobeni(a, b):
    return a * b

def vyhodnoceni(vysledek, odpoved):
    return vysledek == odpoved
body = 0

while True:
    x, y = random.randint(1, 10), random.randint(1, 10)
    vysledek = nasobeni(x, y)
    
    try:
        porovnani = int(input(f"{x} * {y} = "))
        if vyhodnoceni(vysledek, porovnani):
            print("Správně!")
            body += 1
        else:
            print("Nesprávně, zkus to znovu.")
    except ValueError:
        print("Zadej prosím celé číslo.")
    
    pokracovat = input("Chceš pokračovat? (ano/ne): ")
    if pokracovat.lower() != "ano":
        break

print(f"Získal jsi {body} bodů. Hotovo!")

