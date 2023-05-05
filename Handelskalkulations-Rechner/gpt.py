# Vorwärtskalkulation in Python mit tabellarischer Darstellung der Ergebnisse

# Abfrage der Werte
h_lp = float(input("Listenpreis des Händlers: "))
h_rabatt = float(input("Rabatt des Händlers in Prozent: "))
h_skonto = float(input("Skonto des Händlers in Prozent: "))
h_bezug = float(input("Bezugskosten in €: "))
hkz = float(input("Handelskostenzuschlag in Prozent: "))
gewinn = float(input("Gewinn in Prozent: "))
skonto = float(input("Skonto in Prozent: "))
rabatt = float(input("Rabatt in Prozent: "))

# Berechnungen
zp_rabatt = h_lp / 100 * h_rabatt 
zp_rabatt_erg = h_lp - zp_rabatt
bap_skonto = zp_rabatt_erg /100 * h_skonto
bap_skonto_erg = zp_rabatt_erg - bap_skonto
bez_rech_erg = bap_skonto_erg + h_bezug
hk_rech = bez_rech_erg / 100 * hkz
hk_rech_erg = bez_rech_erg + hk_rech
gwn_rech = hk_rech_erg / 100 * gewinn
gwn_rech_erg = hk_rech_erg + gwn_rech
sko_rech_prozent = 100 - skonto
sko_rech = gwn_rech_erg / sko_rech_prozent * skonto
sko_rech_erg = gwn_rech_erg + sko_rech
rab_rech_prozent = 100 - rabatt
rab_rech = sko_rech_erg / rab_rech_prozent * rabatt
rab_rech_erg = sko_rech_erg + rab_rech

# Ausgabe der Ergebnisse in einer Tabelle
print("========================================")
print("                  Ergebnisse            ")
print("========================================")
print("Listenpreis des Händlers:    ", h_lp, "€")
print("Rabatt des Händlers:         ", h_rabatt, "%")
print("Ziel-Listenpreis:            ", zp_rabatt_erg, "€")
print("Skonto des Händlers:         ", h_skonto, "%")
print("Bareinkaufspreis:            ", bap_skonto_erg, "€")
print("Bezugskosten:                ", h_bezug, "€")
print("Bezugspreis:                 ", bez_rech_erg, "€")
print("Handelskostenzuschlag:       ", hkz, "%")
print("Kosten inkl. HKZ:            ", hk_rech_erg, "€")
print("Gewinn:                      ", gewinn, "%")
print("Kalkulierter Verkaufspreis:  ", gwn_rech_erg, "€")
print("Skonto:                      ", skonto, "%")
print("Preis abzüglich Skonto:      ", sko_rech_erg, "€")
print("Rabatt:                      ", rabatt, "%")
print("Preis abzüglich Rabatt:      ", rab_rech_erg, "€")
print("========================================")
