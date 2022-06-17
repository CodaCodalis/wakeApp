import tkinter
import tkinter.messagebox
from tkinter import *

from controller import WakeController
from model.Time import Time


class Frame(Tk):

    def __init__(self):
        super().__init__()
        self.__background = "#00CED1"
        self.columnconfigure(0, weight=1)

    def idk_yet(self):
        self.title("WakeApp")
        self.configure(bg=self.__background)
        self.__init_mainframe()
        self.mainloop()

    def __init_mainframe(self):
        self.__init_label()
        self.__init_entries()
        self.__init_button()

    def __init_label(self):
        sticky = tkinter.W
        padx = 5
        label_title = Label(master=self, text="WakeApp", font=("times", 20, "bold", "italic"),
                            fg="white", bg=self.__background, pady=20)
        label_title.grid(row=0, column=0, columnspan=4)
        label_arrival_time = Label(master=self, text="Bitte geben sie die Ankunfstzeit ein (hh:mm)",
                                   bg=self.__background)
        label_arrival_time.grid(row=1, column=0, sticky=sticky, padx=padx)
        label_duration = Label(master=self, text="Bitte geben sie die Dauer des Fahrtwegs ein (hh:mm)",
                               bg=self.__background)
        label_duration.grid(row=2, column=0, sticky=sticky, padx=padx)
        label_prep_time = Label(master=self, text="Bitte geben sie die Dauer ihrer morgendlicher Routine ein (hh:mm)",
                                bg=self.__background)
        label_prep_time.grid(row=3, column=0, sticky=sticky, padx=padx)
        label_delay = Label(master=self, text="Bitte geben sie die Dauer der Verzögerung ein (hh:mm)",
                            bg=self.__background)
        label_delay.grid(row=4, column=0, sticky=sticky, padx=padx)

    def __init_entries(self):
        pady = 5
        padx = 10
        self.__entry_arrival_time = Entry(master=self, bg="white")
        self.__entry_arrival_time.grid(row=1, column=1, pady=pady, padx=padx)
        self.__entry_duration = Entry(master=self, bg="white")
        self.__entry_duration.grid(row=2, column=1, pady=pady, padx=padx)
        self.__entry_prep_time = Entry(master=self, bg="white")
        self.__entry_prep_time.grid(row=3, column=1, pady=pady, padx=padx)
        self.__entry_delay = Entry(master=self, bg="white")
        self.__entry_delay.grid(row=4, column=1, pady=pady, padx=padx)

    def __init_button(self):
        pady = 30
        clear_button = Button(master=self, text="Eingaben löschen", command=self.__clear_entries)
        clear_button.grid(row=5, column=0, pady=pady)
        calculate_button = Button(master=self, text="Starte Berechnung", command=self.__calculate)
        calculate_button.grid(row=5, column=1, pady=pady, sticky=tkinter.E, padx=10)

    def __clear_entries(self):
        self.__entry_prep_time.delete(0, END)
        self.__entry_arrival_time.delete(0, END)
        self.__entry_duration.delete(0, END)
        self.__entry_delay.delete(0, END)

    def __calculate(self):
        try:
            time = Time(self.__entry_arrival_time.get(),
                        self.__entry_duration.get(),
                        self.__entry_prep_time.get(),
                        self.__entry_delay.get())
            get_up_time = WakeController.computation(time)
            get_up_msg = "Sie müssen um " + str(get_up_time) + " aufstehen!"
            tkinter.messagebox.showinfo(title="Aufstehzeit", message=get_up_msg, bg=self.__background)
            self.__clear_entries()
        except ValueError:
            error_msg = "Mindestens eine Eingabe ist fehlerhaft und entspricht nicht dem vorgegebenen Format (hh:mm)!" \
                        "\nEingaben Wiederholen:"
            tkinter.messagebox.showerror(title="Error", message=error_msg)
        except IndexError:
            error_msg = "Mindestens eine Eingabe ist fehlerhaft und entspricht nicht dem vorgegebenen Format (hh:mm)!" \
                        "\nEingaben Wiederholen:"
            tkinter.messagebox.showerror(title="Error", message=error_msg)
