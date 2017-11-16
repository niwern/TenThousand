import random
import sys
import player
import time
import os


class Game(object):
    value_table = {
        "5": 50,
        "1": 100,
        "222": 200,
        "333": 300,
        "444": 400,
        "555": 500,
        "666": 600,
        "111": 1000,
        "2222": 2000,
        "3333": 3000,
        "4444": 4000,
        "5555": 5000,
        "6666": 6000,
        "1111": 10000,
        "ddddd": 10000
    }
    players = {}
    goal = 10000

    def __init__(self, number=2, goal=100):
        if goal > 10000:
            self.goal = 10000
        else:
            self.goal = goal
        if number < 2:
            print("Es du brauchst mindestens 2 Spieler.")
            number = 2
        for i in range(number):
            self.players[player.Player(str(i+1))] = 0
        self.main()

    @staticmethod
    def roll_the_dice():
        return random.randint(1, 6)

    def reround(self, dices, score):
        if dices < 1:
            dices = 5
        a = str((raw_input("Mit {0} Punkten und {1} Wuerfeln weiter spielen? (Y/N) ".format(score, dices))))
        if a.upper() == 'N':
            return score
        elif a.upper() == 'Y':
            return self.round(dices, score, True)
        else:
            return self.reround(dices, score)

    def round(self, dices, score, go_on):
        if dices < 1:
            dices = 5
        # Mit den Wuerfeln wuerfeln + Ausgabe
        numbers = []
        for dice in range(dices):
            dice = Game.roll_the_dice()
            numbers.append(dice)
        print("Wurfelergebnis = " + str(numbers))

        # Auswertung des Wuerfelns
        stats = {}  # Dicctionary mit ( Augenzahl : Anzahl der Gleichen Augenzahlen )
        for x in numbers:
            if x in stats.keys():
                stats[x] += 1
            else:
                stats[x] = 1

        # Pasch ermitteln
        max_key = stats.keys()[0]  # hoechste Augenzahl
        max_value = stats[stats.keys()[0]]  # hoechste Augenanzahl
        for key in stats.keys():
            if max_value < stats[key]:
                max_value = stats[key]
                max_key = key
        # Pasch analysieren
        if max_value >= 3:
            print("{0}-er Pasch gefunden mit {1}.".format(str(max_value), str(max_key)))
            if max_value == 4:
                x = raw_input("Moechtest du 3 oder 4 Wuerfel zur Seite legen? ")
                if x < 3 or x > 4 or x is None:
                    print("Falsche Eingabe! Du Lappen.")
                    x = 4
            else:
                x = 3
            pasch = str(max_key) * max_value  # Bezeichnung von dem Pasch
            if len(pasch) == 5:
                pasch = 'ddddd'
            score += self.value_table[pasch]  # Punkte fuer den Pasch
            time.sleep(5)
            return self.round(dices - x, score, True)
        # Nach 1 und 5 schauen
        elif 1 in numbers or 5 in numbers:
            score1 = 0
            score5 = 0
            x1 = 0
            x5 = 0
            if 1 in numbers:
                x1 = int(raw_input("Du hast {0} Einser. Wie viele legst du zur Seite? ".format(stats[1])))
                if x1 < 0 or x1 > stats[1]:
                    print("Falsche Eingabe! Du Lappen.")
                    x1 = stats[1]
                score1 = self.value_table["1"] * x1
            if 5 in numbers:
                x5 = int(raw_input("Du hast {0} Fuenfer. Wie viele legst du zur Seite? ".format(stats[5])))
                if x5 < 0 or x5 > stats[5]:
                    print("Falsche Eingabe! Du Lappen.")
                    x5 = stats[5]
                score5 = self.value_table["5"] * x5
            score += score1 + score5
            x = x1 + x5
            if x > 0:
                return self.reround(dices - x, score)
            else:
                return 0
        print("Du hast alles verloren!")
        return 0

    def get_max(self, a):
        max = 0
        for i in a:
            if max < i:
                max = i
        return max

    def main(self):
        while True:
            for p in self.players.keys():
                print("{0} ist am Zug".format(p.name))
                p.total_score += int(self.round(5, 0, True))
                self.players[p] =  p.total_score
                print("Jetztiger Punktestand von {0}: {1}".format(p.name, p.total_score))
                time.sleep(1)
            os.system('clear')
            # Punktezwischenstand
            for p in self.players:
                print("{0} hat {1} Punkte".format(p.name, p.total_score))

            # Kuerung des Gewinners bzw. Fuehrers
            max_score = self.get_max(self.players.values())
            if max_score > self.goal:
                print("------------------------")
                print("Gewinner dieses Matches:")
                print("------------------------")
                for p in self.players.keys():
                    if self.players[p] == max_score:
                        print("{0} : {1}".format(p.name, self.players[p]))
                sys.exit()
            else:
                print("in Fuehrungen:")
                for p in self.players.keys():
                    if self.players[p] == max_score:
                        print("{0} : {1}".format(p.name, self.players[p]))
                print("")


    @staticmethod
    def start():
        goal = raw_input("Wie bis wie hoch sollen die Punkte gehen? ")
        number_of_player = raw_input("Wie viele Spieler seid ihr? ")
        #if goal is not None:
        goal = int(goal)
        #if number_of_player is not None:
        number_of_player = int(number_of_player)
        Game(number_of_player, goal)


Game.start()
