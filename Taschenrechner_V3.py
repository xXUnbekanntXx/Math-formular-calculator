import time
import os
import math

def zuweisung2():
    getos = os.name
    if getos == "nt":
        print("Farb Menü geladen")
        print("Blau [1]         Grün [2]")
        print("Türkis [3]     Rot[4]")
        print("Lila [5]        Gelb[6]")
        print("Standart [7]")
        print("=" * 50)
        color = input(": ")
        if color == "1":
            os.system('color 1')
            zuweisung()
        if color == "2":
            os.system('color 2')
            zuweisung()
        if color == "3":
            os.system('color 3')
            zuweisung()
        if color == "4":
            os.system('color 4')
            zuweisung()
        if color == "5":
            os.system('color 5')
            zuweisung()
        if color == "6":
            os.system('color 6')
            zuweisung()
        if color == "7":
            os.system('color 7')
            zuweisung()
        else:
            os.system('color 7')
            zuweisung()


def zuweisung():
    # Programmwahl
    print("Das ist ein Taschenrechner mit 2 Funktionen")
    print("Wählen sie eins der Folgenden Programmen:")

    print("Taschenrechner (1) ")
    print("Formeln (2) ")
    print("Farben Menü (3) ")
    print("Exit (4) ")
    value1 = int(input("Geben Sie Ihre Wahl jetzt ein: "))

    # Eingabe_Verarbeitung_für_TR
    if value1 == 1:
        print("Eingabe Erfolgreich")

        for x in range(10):
            print(".", flush=True, end="")
            time.sleep(0.5)

        print("Taschenrechner geladen")
        # Taschenrechner
        print("Hallo, das ist eine vereinfachte Version eines Taschenrechners. "
              "Die Benutzung sollte selbsterklärend sein :) ")
        print("                                             ")

        print("Geben Sie die zwei zu verechnenden Zahlen ein.")
        print("                                             ")
        value4 = float(input("Erste Zahl eingeben :"))
        print("                                             ")
        print("Geben Sie die Verechnungsart ein (+;-;/;*)")

        value3 = input()

        value5 = float(input("Zweite Zahl eingeben :"))
        print("                                             ")
        print("Das Ergebnis ist =")
        if value3 == "+":
            print(value4 + value5)
        elif value3 == "-":
            print(value4 - value5)
        elif value3 == "/":
            print(value4 / value5)
        elif value3 == "*":
            print(value4 * value5)

        input("Drücken Sie eine Taste um das Programm neuzustarten")


    # Taschenrechner_Programm_Ende

    # Eingabe_Verabeitung_für_Formeln
    elif value1 == 2:
        print(" ")
        time.sleep(2)
        print(" ")
        print("Mathe Flächen Fomeln (1) ")
        print("Satz des Pythagoras  (2) ")
        print(" ")

        fwahl = int(input("Wählen Sie ein Programm aus: "))

        if fwahl == 1:
            print("                                                    ")

            print("Wählen Sie eines der unten stehenden Flächen Arten.")
            print("                                                    ")
            print("Quadrat               (1) ")
            print("Rechteck              (2) ")
            print("Raute                 (3) ")
            print("Parallelogramm        (4) ")
            print("Trapez                (5) ")
            print("Drachen               (6) ")
            print("Regelmäßiges Sechseck (7) ")
            print("Kreis                 (8) ")
            print("Kreisring             (9) ")
            print("Kreisbogen           (10) ")
            print("Kreisausschnitt      (11) ")

            wahl = int(input("Geben Sie hier ihre Wahl ein: "))

            # Quadrat

            if wahl == 1:
                print("Quadrat wird geladen")
                for x in range(26):
                    print(".", flush=True, end="")
                    time.sleep(0.1)
                print("                     ")
                print(".........................")
                print("Umfang          (1) ")
                print("Flächeninhalt   (2) ")
                print("Diagonale       (3) ")
                print("                    ")

                wahl2 = int(input("Was wollen Sie berechnen?: "))

                # Umfang

                if wahl2 == 1:
                    umf = float(input("Wie läng ist die Seite a?: "))
                    print("Ergebnis = ")
                    print(4 * umf)


                # Flächeninhalt

                elif wahl2 == 2:
                    A = float(input("Wie lang ist Seite a?: "))
                    print("Ergebnis = ")
                    print(A ** 2)


                # Diagonale

                elif wahl2 == 3:
                    D = float(input("Wie lang ist Seite a?: "))
                    print("Ergebnis = ")
                    print((D ** 2 + D ** 2) ** .5)
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Rechteck

            elif wahl == 2:
                print("Rechteck wird geladen")
                for x in range(26):
                    print(".", flush=True, end="")
                    time.sleep(0.1)
                print(".........................")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                print("Diagonale     (3) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite a?: "))
                    zahl2 = float(input("Wie lang ist Seite b?: "))
                    print("Ergebnis = ")
                    print(2 * (zahl1 + zahl2))

                elif wahl3 == 2:
                    zahl3 = float(input("Wie lang ist Seite a?: "))
                    zahl4 = float(input("Wie lang ist Seite b?: "))
                    print("Ergebnis = ")
                    print(zahl3 * zahl4)

                elif wahl3 == 3:
                    zahl5 = float(input("Wie lang ist Seite a?: "))
                    zahl6 = float(input("Wie lang ist Seite b?: "))
                    print("Ergebnis = ")
                    print((zahl5 ** 2 + zahl6 ** 2) ** .5)
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")


            # Raute

            elif wahl == 3:
                print("Raute wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print("                  ")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                # Umfang

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite a?: "))
                    print("Ergebnis = ")
                    print(4 * zahl1)

                # Flächeninhalt

                elif wahl3 == 2:
                    zahl3 = float(input("Wie lang ist Seite a?: "))
                    zahl4 = float(input("Wie lang ist Seite h?: "))
                    print("Ergebnis = ")
                    print(zahl3 * zahl4)

                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")



            # Parallelogramm

            elif wahl == 4:
                print("Parallelogramm wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                # Umfang

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite a?: "))
                    zahl2 = float(input("Wie lang ist Seite b?: "))
                    print("Ergebnis = ")
                    print(2 * (zahl1 + zahl2))

                # Flächeninhalt

                elif wahl3 == 2:
                    zahl3 = float(input("Wie lang ist Seite a?: "))
                    zahl4 = float(input("Wie lang ist Seite h?: "))
                    print("Ergebnis = ")
                    print(zahl3 * zahl4)
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Trapez

            elif wahl == 5:
                print("Trapez wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Umfang          (1) ")
                print("Mittellinie(m) (2) ")
                print("Flächenimhalt   (3) ")
                print("                    ")

                wahl2 = int(input("Was wollen Sie berechnen?: "))

                # Umfang

                if wahl2 == 1:
                    umf = float(input("Wie läng ist die Seite a?: "))
                    zahl2 = float(input("Wie lang ist die Seite b?: "))
                    zahl3 = float(input("Wie lang ist die Seite c?: "))
                    zahl4 = float(input("Wie lang ist die Seite d?: "))

                    print("Ergebnis = ")
                    print(umf + zahl2 + zahl3 + zahl4)


                # Mittellinie (m)

                elif wahl2 == 2:
                    A = float(input("Wie lang ist die Seite a?: "))
                    B = float(input("Wie lang ist die Seite c?: "))
                    print("Ergebnis = ")
                    print(0.5 * (A + B))


                # Flächenimhalt

                elif wahl2 == 3:
                    D = float(input("Wie lang ist die Seite m?: "))
                    B = float(input("Wie lang ist die Seite h?: "))
                    print("Ergebnis = ")
                    print(D * B)
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Drachen

            elif wahl == 6:
                print("Drachen wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                # Umfang

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite a?: "))
                    zahl2 = float(input("Wie lang ist Seite b?: "))
                    print("Ergebnis = ")
                    print(2 * (zahl1 + zahl2))

                # Flächeninhalt

                elif wahl3 == 2:
                    zahl3 = float(input("Wie lang ist Seite e?: "))
                    zahl4 = float(input("Wie lang ist Seite f?: "))
                    print("Ergebnis = ")
                    print(0.5 * (zahl3 * zahl4))
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Regelmäßiges Sechseck

            elif wahl == 7:
                print("Regelmäßiges Sechseck wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                # Umfang

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite a?: "))
                    print("Ergebnis = ")
                    print(6 * zahl1)

                # Flächeninhalt

                elif wahl3 == 2:
                    zahl3 = float(input("Wie lang ist Seite a?: "))
                    print("Ergebnis = ")
                    print(3 / 2 * (zahl3 ** 2) * math.sqrt(3))
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Kreis

            elif wahl == 8:
                print("Kreis wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                # Umfang

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite r?: "))
                    print("Ergebnis = ")
                    print(2 * math.pi * zahl1)

                # Flächeninhalt

                elif wahl3 == 2:
                    zahl3 = float(input("Wie lang ist Seite r?: "))
                    print("Ergebnis = ")
                    print(math.pi * (zahl3 ** 2))
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Kreisring

            elif wahl == 9:
                print("Kreisring wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Umfang        (1) ")
                print("Flächeninhalt (2) ")
                wahl3 = int(input("Was wollen Sie berechnen: "))

                # Umfang

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite r1? (Ring aussen): "))
                    zahl2 = float(input("Wie lang ist Seite r2? (Ring innen) : "))
                    print("Ergebnis = ")
                    print(2 * math.pi * (zahl1 + zahl2))

                # Flächeninhalt

                elif wahl3 == 2:
                    zahl1 = float(input("Wie lang ist Seite r1? (Ring aussen): "))
                    zahl2 = float(input("Wie lang ist Seite r2? (Ring innen) : "))
                    print("Ergebnis = ")
                    print(math.pi * ((zahl1 ** 2) - (zahl2 ** 2)))
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")

            # Kreisbogen

            elif wahl == 10:
                print("Kreisbogen wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                # b = 2*pi*r*(alpha / 360)
                print("Die Variable die ausgerechnet werden soll 0 (Null) eingeben")
                print(" ")
                zahl1 = float(input("Wie lang ist die Seite b?: "))
                zahl2 = float(input("Wie lang ist die Seite r?: "))
                zahl3 = float(input("Wie weit ist der Winkel a (alpha)?: "))

                if zahl1 == 0:
                    print("Ergebnis =")
                    print(2 * math.pi * zahl2 * (zahl3 / 360))

                elif zahl2 == 0:
                    print("Ergebnis =")  # r = (b * 180°) / (Alpha * pi)
                    print((zahl1 * 180) / (zahl3 * math.pi))

                elif zahl3 == 0:
                    print("Ergebnis = ")  # Alpha = (b * 180°) / (pi * r)
                    print((zahl1 * 180) / (math.pi * zahl2))
                input("Drücken Sie Enter um das Programm zu beenden.")


            # Kreisausschnitt

            elif wahl == 11:
                print("Kreisausschnitt wird geladen")
                for x in range(10):
                    print(".", flush=True, end="")
                    time.sleep(0.3)
                print(" ")
                print("Ja        (1) ")
                print("Nein      (2) ")
                wahl3 = int(input("Ist der Kreisbogen angegeben?: "))

                # Kreisbogen angegeben

                if wahl3 == 1:
                    zahl1 = float(input("Wie lang ist Seite r?: "))
                    zahl2 = float(input("Wie lang ist Seite b (Kreisbogen)?: "))
                    print("Ergebnis = ")
                    print((zahl2 * zahl1) / 2)

                # Kreisbogen unbekannt

                elif wahl3 == 2:
                    zahl1 = float(input("Wie lang ist Seite r?: "))
                    zahl2 = float(input("Wie gross ist der Winkel alpha?: "))
                    print("Ergebnis = ")
                    print(math.pi * (zahl1 ** 2) * (zahl2 / 360))
                    print("                ")
                input("Drücken Sie Enter um das Programm zu beenden.")

        elif fwahl == 2:

            print("Satz des Pythagoras")

            print("a**2 * b**2 = c**2 / a^2 + b^2 = c^2")
            # print(3**2) entspricht 3 hoch 2 (zwei ** = hoch)

            print("Geben Sie die Längen der Seiten an, wenn eine Seite nicht gegen ist dann tragen Sie 0 (Null) ein.")
            # ex = exponent
            ex = 2

            seite_a = float(input("Länge der Seite a: "))
            seite_b = float(input("Länge der Seite b: "))
            seite_c = float(input("Länge der Seite c: "))

            if seite_c == 0:
                print("Ergebnis der Seite c = ")
                print((seite_a ** ex + seite_b ** ex) ** .5)

            elif seite_b == 0:
                print("Ergebnis der Seite b = ")
                print((seite_c ** ex - seite_a ** ex) ** .5)

            elif seite_a == 0:
                print("Ergebniss der Seite a =")
                print((seite_c ** ex - seite_b ** ex) ** .5)

            input("Zum beenden des Programmes Enter drücken.")

            # Wurzel ziehen: print( 36 **.5)


    # _Programmstart_Farben_Menü
    elif value1 == 3:
        print("Farben Menü wird gestartet")
        for x in range(10):
            print(".", flush=True, end="")
            time.sleep(0.5)
        zuweisung2()

    # _Exit Programm
    elif value1 == 4:
        print("Programm wird beendet")
        for x in range(3):
            print(".", flush=True, end="")
            time.sleep(0.5)
        exit()


zuweisung()
