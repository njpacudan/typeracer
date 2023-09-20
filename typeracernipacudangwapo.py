import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import *
from datetime import datetime
import time
import random


class TypeRacer:
    def __init__(self):
        self.root = Tk()

        self.root.geometry("+550+315")
        self.menu_frame = Frame(self.root)
        self.menu_frame.grid(column=0, row=0, padx=20, pady=10)
        self.label1 = Label(self.menu_frame, text="TypeRacer",font =('Algerian',14, 'bold'))
        self.label1.grid(row=0, column=0)
        self.play = Button(self.menu_frame, text="PLAY", command= lambda: self.game())
        self.play.grid(row=3, column=0)
        self.quit = Button(self.menu_frame, text="QUIT", command= lambda: self.quit1())
        self.quit.grid(row=4, column=0)
        self.options = Menu(self.menu_frame)
        options1 = Menu(self.options, tearoff=0)
        options1.add_command(label="View Highscore", command=lambda:self.highscore())
        self.options.add_cascade(label="Options", menu=options1)
        self.root.config(menu=self.options)
        self.root.mainloop()
    def game(self):
        self.menu_frame.destroy()
        self.rounds = 1
        self.answer1 = ["She sells seashells on the seashore.","Sphinx of black quartz, judge my vow.", "The quick brown fox jumps over the lazy dog.", "Once upon a midnight dreary, while I pondered, weak and weary.", "While I nodded, nearly napping, suddenly there came a tapping.", "Uh, summa-lumma, dooma-lumma, you assumin' I'm a human.", "Where did you come from, where did you go? Where did you come from, Cotton-Eye Joe?", "However, this valorous visitation of a bygone vexation stands vivified.", "Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality.", "I used to be an adventurer like you, until I took an arrow to the knee.","But then there was Fire and with fire came disparity.", "Thus began the Age of Fire. But soon the flames will fade and only Dark will remain.","Yesterday was history, tomorrow is a mystery, and today is a gift. That's why it is called the present.","Why did you make me do this? You're fighting so you can watch everyone around you die. Think, Mark!","Taste from the tallest chalice, dine at the largest halls. And all I ask in return is your soul.", "Flower gleam and glow, let your powers shine, make the clock reverse, bring back what once was mine", "Nanomachines, son! They harden in response to physical trauma! You can't hurt me, Jack!", "Aren't we forgetting one teensy-weensy but ever-so-crucial little tiny detail?","Finally! A worthy opponent! Our battle will be legendary!", "If you can't make the most out of any given moment, then you don't deserve a single extra second.","Does the wind flee? Or does it follow?","They laugh. And scream! And dance. And flee!","And everywhere Lamb went. Wolf was sure to follow!","How can a clam cram in a clean cream can?","Curiosity killed the cat but satisfaction brought it back.","Great minds think alike but fools rarely differ.","The early bird catches the worm, but the second mouse gets the cheese.","That mountain you've been carrying, you were only suppose to climb.","The axe forgets; the tree remembers.","With great power comes great responsibility."]
        self.chance = random.choice(self.answer1)
        self.empty = ""
        self.root.geometry("+500+315")
        self.game_frame = Frame(self.root)
        self.game_frame.grid(column=0, row=0, padx=20, pady=5)
        messagebox.showinfo("TypeRacer","Test your typing speed by typing various texts as fast as possible.")
        self.start = time.time()
        self.answer = StringVar()
        self.root.title("TypeRacer || Round "+str(self.rounds))
        self.question = Label(self.game_frame, text=self.chance)
        self.question.grid(row=0, column=0)
        self.answer = Entry(self.game_frame, width=80)
        self.answer.grid(row=2, column=0)
        self.answer_button = Button(self.game_frame, text="Submit", command=self.check_answer)
        self.answer_button.grid(row=3, column=0)
        self.clear_button = Button(self.game_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=4, column=0)
        self.quit = Button(self.game_frame, text="Quit", command=lambda: self.quit1())
        self.quit.grid(row=4, column=1)

    def check_answer(self):
        if self.answer.get() == self.chance:
            messagebox.showinfo("You got it right!","Proceeding to the next round.")
            self.chance = "                                                                                                                                                                                       "
            self.question = Label(self.game_frame, text=self.chance)
            self.question.grid(row=0, column=0)
            self.chance = random.choice(self.answer1)
            self.question = Label(self.game_frame, text=self.chance)
            self.question.grid(row=0, column=0)
            self.answer = Entry(self.game_frame, width=80)
            self.answer.grid(row=2, column=0)
            self.rounds += 1
            self.root.title("TypeRacer || Round " + str(self.rounds))
            if self.rounds == 6:  # Change the maximum amount of rounds here!
                self.end = time.time()
                self.question.grid_forget()
                self.answer_button.grid_forget()
                self.answer.grid_forget()
                self.clear_button.grid_forget()
                f1 = self.end - self.start
                f2 = int(f1)
                f2 = datetime.fromtimestamp(f2)
                self.f3 = f2.strftime("%M:%S")
                self.root.title("Well done!")
                asd = Label(self.game_frame, text="                                                                                                                                                                ")
                asd.grid(row=2,column=0)
                end = Label(self.game_frame, text="Congratulations! Your total time was: " + str(self.f3))
                end.grid(row=2, column=0)
                return_mainmenu = Button (self.game_frame, text="Return to Menu", command=lambda: self.switch())
                return_mainmenu.grid(row=4, column=0)
                score = self.f3

                with open("highscore.txt", "r+") as self.high:
                    self.high1 = self.high.read()
                    if not self.high1:
                        self.high1 = '00:00'
                    if score < self.high1:
                        Label(self.game_frame, text="New Highscore!").grid(row=0, column=0)
                        self.high.seek(0)
                        self.high.write(str(score))
                        self.high.truncate()

        else:
            messagebox.showerror("Error!","Incorrect input!")

    def highscore(self):
        highsc = open("highscore.txt","r")
        messagebox._show("Highscore","Highscore is based on how fast you finished. \nCurrent highscore: " + highsc.read())
    def clear(self):
        self.answer = Entry(self.game_frame, width=80)
        self.answer.grid(row=2, column=0)
    def switch(self):
        self.root.destroy()
        open(self.__init__())
    def quit1(self):
        exit()

if __name__== '__main__':
    gui = TypeRacer()