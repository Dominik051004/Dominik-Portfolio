import random

def gib_hinweis(geheimzahl, tipp, versuch):
    hinweise = []

    if tipp < geheimzahl:
        hinweise.append("Die gesuchte Zahl ist größer.")
    elif tipp > geheimzahl:
        hinweise.append("Die gesuchte Zahl ist kleiner.")

    # Zusätzliche Hinweise, die mit jedem Versuch mehr Informationen geben
    if versuch >= 2:
        if geheimzahl % 2 == 0:
            hinweise.append("Die gesuchte Zahl ist gerade.")
        else:
            hinweise.append("Die gesuchte Zahl ist ungerade.")

    if versuch >= 3:
        if geheimzahl % 3 == 0:
            hinweise.append("Die gesuchte Zahl ist durch 3 teilbar.")
        elif geheimzahl % 5 == 0:
            hinweise.append("Die gesuchte Zahl ist durch 5 teilbar.")

    if versuch >= 4:
        if geheimzahl < 50:
            hinweise.append("Die Zahl ist kleiner als 50.")
        else:
            hinweise.append("Die Zahl ist 50 oder größer.")

    return " ".join(hinweise)

def ist_zahl(eingabe):
    try:
        int(eingabe)
        return True
    except ValueError:
        return False

def spiel_starten():
    geheimzahl = random.randint(1, 100)
    versuche = 0

    print("Willkommen beim Zahlenraten!")
    print("Ich habe eine Zahl zwischen 1 und 100 ausgewählt. Kannst du sie erraten?")

    while True:
        eingabe = input("Dein Tipp: ")

        if not ist_zahl(eingabe):
            print("Bitte gib eine gültige Zahl ein.")
            continue

        tipp = int(eingabe)
        versuche += 1

        if tipp == geheimzahl:
            print(f"Du hast richtig geraten! Die Zahl war {geheimzahl}.")
            print(f"Du hast {versuche} Versuche gebraucht.")
            break
        else:
            hinweis = gib_hinweis(geheimzahl, tipp, versuche)
            print(hinweis)

spiel_starten()