import random
import player


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

    def __init__(self, number):
        if number < 2:
            print("Es du brauchst mindestens 2 Spieler.")
            number = 2
        players = [player.Player("1"), player.Player("2")]
        for i in range(number - 2):
            p = player.Player(str(i+3))
            players.append(p)
        self.main(players)

    @staticmethod
    def roll_the_dice():
        return random.randint(1, 6)

    def round(self, dices, score):
        print("start " + str(score))
        # Wieder alle Wuerfel nehmen
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
                x = int(raw_input("Moechtest du 3 oder 4 Wuerfel zur Seite legen? "))
                if x < 3 or x > 4:
                    print("Falsche Eingabe! Du Lappen.")
                    x = 4
            else:
                x = 3
            # Todo Pasch ddddd
            pasch = str(max_key) * max_value  # Bezeichnung von dem Pasch
            if len(pasch) == 5:
                pasch = 'ddddd'
            score += self.value_table[pasch]  # Punkte fuer den Pasch
            print(score)
            return self.round(dices - x, score)
        elif 1 in numbers or 5 in numbers:
            score1 = 0
            score5 = 0
            x1 = 0
            x5 = 0
            if 1 in numbers:
                x1 = int(raw_input("Du hast {0} Einser gewuerfelt. Wie viele moechtest du zur Seite legen".format(stats[1])))
                if x1 < 0 or x1 > stats[1]:
                    print("Falsche Eingabe! Du Lappen.")
                    x1 = stats[1]
                score1 = self.value_table["1"] * x1
            if 5 in numbers:
                x5 = int(raw_input("Du hast {0} Fuenfer gewuerfelt. Wie viele moechtest du zur Seite legen".format(stats[5])))
                if x5 < 0 or x5 > stats[5]:
                    print("Falsche Eingabe! Du Lappen.")
                    x5 = stats[5]
                score5 = self.value_table["5"] * x5
            score += score1 + score5
            print(score)
            x = x1 + x5
            if x > 0:
                return self.round(dices - x, score)
            else:
                return score
        return 0

    def main(self, players):
        while True:
            for p in players:
                print("{0} ist am Zug".format(p.name))
                p.total_score += self.round(5, 0)
                print(p.total_score)

            # Punktezwischenstand
            max = 0
            max_p = None
            for p in players:
                print("{0} hat {1} Punkte".format(p.name, p.total_score))
                if p.total_score > max:
                    max_p = p
                    max = p.total_score

            # Todo kuere den Gewinner
            if max >= 10000:
                print("{0} hat mit {1} Punkten gewonnen".format(max_p.name, max))
            else:
                print("{0} fuehrt mit {1} Punkten".format(max_p.name, max))

Game(1)
