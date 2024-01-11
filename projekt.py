import csv

def minden_adat_listazasa(adatok):
    for adat in adatok:
        print(adat)

def adatok_mentese_fajlba(adatok, fajlnev):
    with open(fajlnev, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for adat in adatok:
            csvwriter.writerow(adat)

def idotartomanyban_levo_adatok(adatok, kezdo_ev, vegso_ev):
    for adat in adatok:
        evszam = int(adat[0])  # Feltételezzük, hogy az év az adatok első eleme
        if kezdo_ev <= evszam <= vegso_ev:
            print(adat)

def tudasteszt(adatok):
    evszamok = [adat[0] for adat in adatok]
    valasztott_evszam = random.choice(evszamok)
    helyes_vivmanyok = [adat[1] for adat in adatok if adat[0] == valasztott_evszam]
    veletlen_vivmanyok = random.sample(adatok, 2)
    
    kerdes = f"Adja meg a(z) {valasztott_evszam} évben elért vívmányt: "
    valaszok = [vivmany[1] for vivmany in veletlen_vivmanyok]
    valaszok.append(helyes_vivmanyok[0])

    random.shuffle(valaszok)
    
    print(kerdes)
    for i, valasz in enumerate(valaszok):
        print(f"{i+1}. {valasz}")
    
    felhasznalo_valasz = input("Válasz: ")
    
    if helyes_vivmanyok[0] == valaszok[int(felhasznalo_valasz)-1]:
        print("Helyes válasz!")
    else:
        print("Rossz válasz. A helyes válasz: ", helyes_vivmanyok[0])

# Példa adatok
adatok = [
    [1800, "Első vívmány"],
    [1850, "Második vívmány"],
    [1900, "Harmadik vívmány"],
    # További adatok...
]

while True:
    print("\n1. Minden adat listázása a képernyőre")
    print("2. Minden adat listázása egy fájlba")
    print("3. Adott időtartományban lévő vívmányok listázása")
    print("4. Tudásteszt")
    print("0. Kilépés")

    valasztas = input("Válasszon egy menüpontot: ")

    if valasztas == "1":
        minden_adat_listazasa(adatok)
    elif valasztas == "2":
        fajlnev = input("Adja meg a kimeneti fájl nevét: ")
        adatok_mentese_fajlba(adatok, fajlnev)
    elif valasztas == "3":
        kezdo_ev = int(input("Adja meg a kezdő évszámot: "))
        vegso_ev = int(input("Adja meg a végső évszámot: "))
        idotartomanyban_levo_adatok(adatok, kezdo_ev, vegso_ev)
    elif valasztas == "4":
        tudasteszt(adatok)
    elif valasztas == "0":
        break
    else:
        print("Érvénytelen választás. Kérem, válasszon újra.")
