import sys

try:
    nummer1 = int(input("Erste Zahl:"))
except ValueError:
    print("#####   Eine Zahl eingeben!   ####")
    sys.exit(1)


operator = input("Wähle einen Operator:")

if operator == "+" or "-" or "*" or ":":
    print(operator)
else:
    print("Es handelt sich hier um kein Valides Zeichen! Nutze + - * :")
    sys.exit(1)


try:
    nummer2 = int(input("Zweite Zahl:"))
except ValueError:
    print("#####   Eine Zahl eingeben!   ####")
    sys.exit(1)

if operator == "+":
    erghebnis = nummer1 + nummer2
elif operator == "-":
    erghebnis = nummer1 - nummer2
elif operator == "*":
    erghebnis = nummer1 * nummer2
elif operator == ":":
    erghebnis = nummer1 / nummer2

print("ergebnis", erghebnis)