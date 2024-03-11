import random

def nasobeni(a, b):
    return a * b

def deleni(a, b):
    if b == 0:
        return "Nelze dělit nulou!"
    else:
        return a / b

def scitani(a, b):
    return a + b

def odecitani(a, b):
    return a - b

def vyhodnoceni(vysledek, odpoved):
    return vysledek == odpoved

body = 0

while True:
    x, y = random.randint(1, 10), random.randint(1, 10)
    operace = input("Vyber operaci (+, -, *, /): ")
    
    if operace == '+':
        vysledek = scitani(x, y)
    elif operace == '-':
        vysledek = odecitani(x, y)
    elif operace == '*':
        vysledek = nasobeni(x, y)
    elif operace == '/':
        vysledek = deleni(x, y)
    else:
        print("Neplatná operace. ")
        
    
    try:
        porovnani = float(input(f"{x} {operace} {y} = "))
        if vyhodnoceni(vysledek, porovnani):
            print("Spravně!")
            body += 1
        else:
            print("Nespravně, zkus to znovu.")
    except :
        print("Zadej prosím číslo.")
    
    
    pokracovat = input("Chceš pokračovat? (ano/ne): ")
    if pokracovat.lower() != "ano":
        print("porovnani ukončeno")
        break
    
print(f"Získal jsi {body} bodů. Hotovo!")
