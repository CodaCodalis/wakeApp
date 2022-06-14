from Time import *
from WakeController import computation


class Menu:
    def data_query(self):
        arrivalTime = input("Gib die Zielzeit ein (Format: hh:mm):\n")
        duration = input("Gib die Dauer ein (Format: hh:mm):\n")
        prepTime = input("Gib die Vorbereitungszeit ein (Format: hh:mm):\n")
        delay = input("Gib die Verzögerungen ein (Format: hh:mm):\n")
        try:
            time = Time(arrivalTime, duration, prepTime, delay)
            get_up_time = computation(time)
            print(f'Stehe um {get_up_time} auf!\n')
        except ValueError:
            print("Mindestens eine Eingabe ist fehlerhaft und entspricht nicht dem vorgegebenen Format (hh:mm)!")
            print("Eingabe Wiederholen:")
        except IndexError:
            print("Mindestens eine Eingabe ist fehlerhaft und entspricht nicht dem vorgegebenen Format (hh:mm)!")
            print("Eingabe Wiederholen:")

    def banner(self):
        welcomeMes = "###### Herzlich Willkommen zur WakeApp Terminal App ######"
        print(welcomeMes)
        print("-" * len(welcomeMes) + "\n")
        print("Gib die benötigten Daten ein.\n")