import random
import sys
import time
import os
from Tkinter import *

import player
import window

def clicking_action():
    print("Hallo I bims der Fun")


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
    players = {}  # player : score
    goal = 10000

    def __init__(self, number=2, goal=10000):
        self.goal = goal
        if number < 2:
            print("at least 2 player")
            number = 2
        for i in range(number):
            self.players[player.Player(str(i+1))] = 0
        fenster = window.Window()
        self.main()


    def roll_the_dice(self):
        return random.randint(1, 6)

    def reround(self, dices, score):
        if dices < 1:
            dices = 5
        a = str((raw_input("continue with\n\t {0} points & \n\t {1} \t dices? (Y/N) ".format(score, dices))))
        if a.upper() == 'N':
            return score
        elif a.upper() == 'Y':
            return self.round(dices, score)
        else:
            return self.reround(dices, score)

    def round(self, dices, score):
        if dices < 1:
            dices = 5
        # Mit den Wuerfeln wuerfeln + Ausgabe
        numbers = []
        for dice in range(dices):
            dice = self.roll_the_dice()
            numbers.append(dice)
        numbers.sort()
        print("\t\t" + str(numbers))
        # self.fenster.anweisungs_label.config(text= str(numbers))

        # Auswertung des Wuerfelns
        stats = {1: 0, 5: 0}  # Dicctionary mit ( Augenzahl : Anzahl der Gleichen Augenzahlen )
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
            print("{0} of the kind: {1}.".format(str(max_value), str(max_key)))
            if max_value == 4:
                x = int(raw_input("take 3 or 4 dices: "))
                # Lappentest
                if 3 > x or x > 4 or x is None:
                    print("Falsche Eingabe! Du Lappen.")
                    x = 4
            else:
                x = 3
            pasch = str(max_key) * max_value  # Bezeichnung von dem Pasch
            if len(pasch) == 5:
                pasch = 'ddddd'
            score += self.value_table[pasch]  # Punkte fuer den Pasch
            time.sleep(5)
            return self.round(dices - x, score)
        # Nach 1 und 5 schauen
        elif 1 in numbers or 5 in numbers:
            if 1 in numbers and 5 in numbers:
                out = "{0}x 1 \t{1}x 5\t={2} take: ".format(stats[1], stats[5], stats[1] + stats[5])
            elif 1 in numbers:
                out = "{0}x 1 \ttake:  ".format(stats[1])
            else:
                out = "{0}x 5 \ttake: ".format(stats[5])

            try:
                x = int(raw_input(out))
            except ValueError:
                x = stats[1] + stats[5]

            # Lappentest
            if 0 > x or x > (int(stats[1] + stats[5])):
                print("Falsche Eingabe! Du Lappen.")
                x = int(stats[1]) + int(stats[5])
            if x == 0:
                return 0

            dices -= x  #  x wuerfel entfernen
            # score erhoehen
            for i in range(stats[1]):
                score += self.value_table["1"]
                x -= 1
            score += self.value_table["5"] * x
            return self.reround(dices, score)
        print("You lost everything!")
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
                print("{0}'s turn:".format(p.name))
                p.total_score += int(self.round(5, 0))
                self.players[p] =  p.total_score
                print("score:  {0}: {1}\n".format(p.name, p.total_score))
                time.sleep(.5)
            os.system('clear')
            # Punktezwischenstand
            for p in self.players:
                print("{0} has {1} points".format(p.name, p.total_score))

            # Kuerung des Gewinners bzw. Fuehrers
            max_score = self.get_max(self.players.values())
            if max_score > self.goal:
                print("-----------------------")
                print("Winner of this Matches:")
                print("-----------------------")
                for p in self.players.keys():
                    if self.players[p] == max_score:
                        print("{0} : {1}".format(p.name, self.players[p]))
                sys.exit()
            else:
                print("in lead:")
                for p in self.players.keys():
                    if self.players[p] == max_score:
                        print("\t {0} with {1}".format(p.name, self.players[p]))
                print("")


def start():
    Game()
    try:
        goal = int(raw_input("How hight is the goal? \t"))
    except ValueError:
        goal = 10000
    try:
        number_of_player = int(raw_input("How many player? \t\t"))
    except ValueError:
        number_of_player = 2
    Game(int(number_of_player), int(goal))


start()
