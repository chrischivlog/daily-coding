import sys

try:
    nummer1 = int(input("Erste Zahl:"))
except ValueError:
    print("#####   Eine Zahl eingeben!   ####")
    sys.exit(1)


operator = input("Wähle einen Operator:")

if operator == "+" and "-" and "*" and ":":
    print(operator)
else:
    print("Es handelt sich hier um kein Valides Zeichen! Nutze + - * :")
    sys.exit(1)


try:
    nummer2 = int(input("Zweite Zahl:"))
except ValueError:
    print("#####   Eine Zahl eingeben!   ####")
    sys.exit(1)

erghebnis = nummer1 'operator' nummer2

print(erghebnis)