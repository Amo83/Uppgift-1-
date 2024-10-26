konton = [
    {"kontonummer": "1", "namn": "AMER HAIDAR", "lösenord": "1234", "saldo": 1000},
    {"kontonummer": "2", "namn": "JOHN SMITH", "lösenord": "4321", "saldo": 500},
]




def mainmenu():
    global userinput
    print(" ")
    print("Welcome to Amer Bank")
    print("----------------------")
    print(" ")
    print("1- Skapa konto")
    print("2- Administrera konto")
    print("3- Avsluta")
    print("----------------------")
    print(" ")

    userinput = input("Välj ett alternativ... \n")

while True:
    
    mainmenu()

    if userinput == '1':
        print("Skapa konto")
        print("----------------")
        print("Ange kontonummer")
        kontonummer = input()
        for i in konton:
            if i["kontonummer"] == kontonummer:
                print("Kontonummer finns redan")
                break
            else:
                print("Ange namn i stora bokstäver:")
                namn = input().upper()
                print("Ange lösenord:")
                lösenord = input()
                print("Ange saldo:")
                try:
                    saldo = int(input())
                except ValueError:
                    print("Ange saldo med siffror")
                    

            
                konton.append({"kontonummer": kontonummer, "namn": namn, "lösenord": lösenord, "saldo": saldo})
                print("Konto skapat")
                break
            
    elif userinput == '2':
        print("Administrera konto")
        selectedkontonummer = input("Ange konto nummer i siffror...")
        for i in konton:
                if i["kontonummer"] == selectedkontonummer:
                    print("")
                    print("Konto hittat")
                    print("-------------------")
                    print("")
                    print("1- Visa saldo")
                    print("2- Sätt in pengar")
                    print("3- Ta ut pengar")
                    print("")
                    userinput = input("Välj ett alternativ...")
                    if userinput == '1':
                        print("Dins saldo är:", i["saldo"])
                        input("Tryck enter för att förtsätta...")
                        continue
                    elif userinput == '2':
                        print("Sätt in pengar")
                        print("-------------------")
                        print("Ange belopp")
                        belopp = int(input())
                        if belopp < 0:
                            print("Ange ett positivt belopp")
                            input("Tryck enter för att förtsätta...")
                            continue
                        else:
                            i["saldo"] += belopp
                            print("Du har satt in", belopp, "kr")
                            print("Tyvärr kan vi inte ge kvitton men din saldo är nu:", i["saldo"])
                            input("Tryck enter för att förtsätta...")
                            continue
                    elif userinput == '3':
                        print("Ta ut pengar")
                        print("-------------------")
                        print("Ange belopp")
                        belopp = int(input())
                        if belopp > i["saldo"]:
                            print("Du har inte tillräckligt pengar")
                            input("Tryck enter för att förtsätta...")
                            continue
                        else:
                            i["saldo"] -= belopp
                            print("Du har tagit ut", belopp, "kr")
                            print("Tyvärr kan vi inte ge kvitton men din saldo är nu:", i["saldo"])
                            input("Tryck enter för att förtsätta...")
                            continue
        else:
            print("Konto hittades inte")
            continue
    elif userinput == '3':
        continue
    else:
        print("Ogiltigt val")



