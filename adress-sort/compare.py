import csv
import os

#print(os.listdir('./'))

# Pfade der Eingabedateien und der Ausgabedatei
datei_adress = 'adress-sort/input.csv'
datei_ref = 'adress-sort/reference.csv'
ausgabe_pfad = 'ergaenzte_datei_b.csv'

# Lese Datei A in ein Dictionary für schnellen Zugriff
adressen_a = {}
with open(datei_adress, mode='r', encoding='utf-8') as datei_a:
    
    reader = csv.reader(datei_a, delimiter=';')
    for ort, teilort, strasse in reader:
        adressen_a[(ort, strasse)] = teilort

# Verarbeite Datei B und ergänze fehlende Teilorte aus Datei A
with open(datei_ref, mode='r', encoding='utf-8') as datei_b, \
        open(ausgabe_pfad, mode='w', encoding='utf-8', newline='') as ausgabe_datei:
    
    reader = csv.reader(datei_b, delimiter=';')
    writer = csv.writer(ausgabe_datei, delimiter=';')

    for ort, teilort, strasse in reader:
        if teilort == '' and (ort, strasse) in adressen_a:  # Prüfe, ob Teilort fehlt und in A vorhanden ist
            teilort = adressen_a[(ort, strasse)]
        writer.writerow([ort, teilort, strasse])

