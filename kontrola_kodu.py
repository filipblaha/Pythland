def trideni_souboru(vstupni_soubor):
    otevrene_soubory = {}

    with open(vstupni_soubor, "r") as raw_can:
        radky = raw_can.readlines()

    for radek in radky:
        casti = radek.split()
        if len(casti) <= 21:
            pass
        else:
            CANID = casti[22]


            if CANID not in otevrene_soubory:
                print(f"Název té can zprávy = '{CANID}'")
                jmeno_souboru = input("Zadejte název souboru plz: ")
                soubor = open(jmeno_souboru, "w")
                otevrene_soubory[CANID] = soubor

            # Zapište aktuální řádek do příslušného souboru
            soubor = otevrene_soubory[CANID]
            soubor.write(radek)

    for soubor in otevrene_soubory.values():
        soubor.close()


trideni_souboru("can_message.txt")
