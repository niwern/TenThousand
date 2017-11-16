class Player(object):
    total_score = 0
    name = ""

    def __init__(self, name):
        input = raw_input("Geben Sie einen Spielernamen ein: ")
        if input != "":
            self.name = input
        else:
            self.name = name

    def add_points(self, points):
        self.total_score += points
