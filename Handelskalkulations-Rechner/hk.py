h_lp = float(input("Listenpreis des Händlers: "))
h_rabatt = float(input("Rabbat des Händlers: "))
h_skonto = float(input("Skonto des Händlers: "))
h_bezug = float(input("Bezugskosten in €: "))
hkz = float(input("Handelskostenzuschlag: "))
gewinn = float(input("Gewinn: "))
skonto = float(input("Skonto: "))
rabatt = float(input("Rabatt: "))

### Errechenen des Zieleinkaufspreises

zp_rabatt = h_lp / 100 * h_rabatt 
zp_rabatt_erg = h_lp - zp_rabatt

### Errechnen des Bareinkaufspreis

bap_skonto = zp_rabatt_erg /100 * h_skonto
bap_skonto_erg = zp_rabatt_erg - bap_skonto

### Errechenen des Bezugspreises

bez_rech_erg = bap_skonto_erg + h_bezug

### Errechnen Handelskostenzuschlag

hk_rech = bez_rech_erg / 100 * hkz
hk_rech_erg = bez_rech_erg + hk_rech

### Errechnen des Gewinns

gwn_rech = hk_rech_erg / 100 * gewinn
gwn_rech_erg = hk_rech_erg + gwn_rech

### Errechnen des skontos

sko_rech_prozent = 100 - skonto
sko_rech = gwn_rech_erg / sko_rech_prozent * skonto
sko_rech_erg = gwn_rech_erg + sko_rech

### Errechnen des rabatt

rab_rech_prozent = 100 - rabatt
rab_rech = sko_rech_erg / rab_rech_prozent * rabatt
rab_rech_erg = sko_rech_erg + rab_rech


print(rab_rech_erg)