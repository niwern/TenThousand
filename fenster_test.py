from Tkinter import *
"""
Fenster
- hat ein leatherboard auf der linken Seite nach Punkten geordnet
- hat ein button zum wuerfeln
- hat nach dem wuerfeln eine bestimmte Anzahl an Wuerfeln und zugehoerig jeweils ein "pick"-button
- hat bei einem pasch nur einen "pick_pasch" button, bei 4er Pasch: "pick_3_pasch" und "pick_4_pasch"
"""



class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        mainloop()

    def click(self):
        hallo = eingabefeld.get()
        lable.config(text= "Du hast es getan!! " + hallo)
# """
fenster = Window()
lable = Label (fenster, text=" descreptiver Text zu der mometaigen Situation")
button1 = Button(fenster, text= "Button", command = fenster.click)
eingabefeld = Entry(fenster, bd=5, width=40)
lable.pack()
button1.pack()
eingabefeld.pack()
fenster.mainloop()
# """






"""
    
    lable = Label()
    feld = Entry()
    #fenster = Tk()


    def __init__(self):
        self.title("Nur ein Fenster")

        change_button = Button(fenster, text="Aendern", command=button_action)
        exit_button = Button(fenster, text="Beenden", command=fenster.quit)
        anweisungs_label = Label(fenster, text="Ich bin eine Anweisung:\n\
                                    Klicke auf 'Aendern'.")
        self.lable = anweisungs_label
        eingabefeld = Entry(fenster, bd=5, width=40)
        info_label = Label(fenster, text="Ich bin eine Info:\n\
                            Der Beenden Button schliesst das Programm.")
        anweisungs_label.pack()
        change_button.pack()
        eingabefeld.pack()
        info_label.pack()
        exit_button.pack()


        # In der Ereignisschleife auf Eingabe des Benutzers warten.
        self.mainloop()

    def button_action(self):
        input1 = self.feld.get()
        self.label.config(text="Ich wurde geaendert, zu: " + input1 + "!")


fenster = 
"""