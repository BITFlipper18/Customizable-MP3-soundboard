from tkinter import *
from pygame import mixer
import tkinter

#COLUMN1 = demon
#COLUMN2 = animals
#COLUMN3 = nature
#COLUMN4 = soundeffects


class AnimalSounds:

    def __init__(self, master):
        master = tkinter.Tk()
        master.title("DnD's sound board")
        master.geometry("500x350")

# COLUMN1 = demon

        self.Demon_COLUMN = tkinter.Button(master, text="Demon_COLUMN")
        self.Demon_COLUMN.grid(row=0, column=1)

        self.Demon_I_am_death = tkinter.Button(master, text="Demon_I_am_death", command=self.Demon_I_am_death)
        self.Demon_I_am_death.grid(row=1, column=1)

        self.Demon_I_am_invincible = tkinter.Button(master, text="Demon_I_am_invincible", command=self.Demon_I_am_invincible)
        self.Demon_I_am_invincible.grid(row=2, column=1)

        self.Demon_I_am_the_darkness = tkinter.Button(master, text="Demon_I_am_the_darkness", command=self.Demon_I_am_the_darkness)
        self.Demon_I_am_the_darkness.grid(row=3, column=1)

        self.Demon_I_will_kill_you = tkinter.Button(master, text="Demon_I_will_kill_you", command=self.Demon_I_will_kill_you)
        self.Demon_I_will_kill_you.grid(row=4, column=1)

        self.Demon_Im_coming_for_you_now = tkinter.Button(master, text="Demon_Im_coming_for_you_now", command=self.Demon_Im_coming_for_you_now)
        self.Demon_Im_coming_for_you_now.grid(row=5, column=1)

        self.Demon_Welcome_to_hell = tkinter.Button(master, text="Demon_Welcome_to_hell", command=self.Demon_Welcome_to_hell)
        self.Demon_Welcome_to_hell.grid(row=6, column=1)

        self.Demon_You_are_dead = tkinter.Button(master, text="Demon_You_are_dead", command=self.Demon_You_are_dead)
        self.Demon_You_are_dead.grid(row=7, column=1)

        self.Demon_You_are_next = tkinter.Button(master, text="Demon_You_are_next", command=self.Demon_You_are_next)
        self.Demon_You_are_next.grid(row=8, column=1)

        self.Demon_You_have_not_defeated_me_yet = tkinter.Button(master, text="Demon_You_have_not_defeated_me_yet", command=self.Demon_You_have_not_defeated_me_yet)
        self.Demon_You_have_not_defeated_me_yet.grid(row=9, column=1)

        # COLUMN2 = animals

        self.Animal_COLUMN = tkinter.Button(master, text="Animal_COLUMN")
        self.Animal_COLUMN.grid(row=0, column=2)

        self.Cat_Growls = tkinter.Button(master, text="Cat_Growls", command=self.Cat_Growls)
        self.Cat_Growls.grid(row=1, column=2)

        self.Cat_Screams = tkinter.Button(master, text="Cat_Screams", command=self.Cat_Screams)
        self.Cat_Screams.grid(row=2, column=2)

        self.Dog_Angry = tkinter.Button(master, text="Dog_Angry", command=self.Dog_Angry)
        self.Dog_Angry.grid(row=3, column=2)

        self.Witch_Laugh = tkinter.Button(master, text="Witch_Laugh", command=self.Witch_Laugh)
        self.Witch_Laugh.grid(row=4, column=2)


    def Cat_Growls(self):
        mixer.music.load("Cat_Growls.mp3")
        mixer.music.play()
        print("Button works!")


    def Cat_Screams(self):
        mixer.music.load("Cat_Screams.mp3")
        mixer.music.play()
        print("Button works!")

    def Dog_Angry(self):
        mixer.music.load("Dog_Angry.mp3")
        mixer.music.play()
        print("Button works!")

    def Witch_Laugh(self):
        mixer.music.load("Witch_Laugh.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_I_am_death(self):
        mixer.music.load("Demon_I_am_death.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_I_am_invincible(self):
        mixer.music.load("Demon_I_am_invincible.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_I_am_the_darkness(self):
        mixer.music.load("Demon_I_am_the_darkness.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_I_will_kill_you(self):
        mixer.music.load("Demon_I_will_kill_you.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_Im_coming_for_you_now(self):
        mixer.music.load("Demon_Im_coming_for_you_now.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_Welcome_to_hell(self):
        mixer.music.load("Demon_Welcome_to_hell.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_You_are_dead(self):
        mixer.music.load("Demon_You_are_dead.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_You_are_next(self):
        mixer.music.load("Demon_You_are_next.mp3")
        mixer.music.play()
        print("Button works!")

    def Demon_You_have_not_defeated_me_yet(self):
        mixer.music.load("Demon_You_have_not_defeated_me_yet.mp3")
        mixer.music.play()
        print("Button works!")




root = tkinter.Frame()
mixer.init() #initializing the mixer
a = AnimalSounds(tkinter) #Initiates frame with sounds to pop up!
root.mainloop()
