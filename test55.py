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

for _ in range(10):
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
        print("Neplatná operace. Zadejte prosím platnou operaci.")
        continue
    
    try:
        porovnani = float(input(f"{x} {operace} {y} = "))
        if vyhodnoceni(vysledek, porovnani):
            print("Správně!")
            body += 1
        else:
            print("Nesprávně, zkus to znovu.")
    except ValueError:
        print("Zadej prosím číslo.")

print(f"Získal jsi {body} bodů. Hotovo!")
