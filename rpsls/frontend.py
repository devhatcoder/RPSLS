#!/usr/bin/env python
'''
    This module contains the GUI application for the game.
'''
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from random import choice

from rpsls.backend import Ruleset


# Choices
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
LIZARD = 'Lizard'
SPOCK = 'Spock'
# Image files directory
IMG_FILES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'images')


class AppGui:

    def __init__(self, ruleset: Ruleset) -> None:

        self.ruleset = ruleset

        self.main_window = tk.Tk()
        self.main_window.geometry("680x440")
        self.main_window.title("RPSLS")

        self.title_label = tk.Label(self.main_window,
                                    text="Rock Paper Scissors Lizard Spock!",
                                    font=('Arial', 24))
        self.title_label.pack(padx=20, pady=25)

        self.instruction_label = tk.Label(self.main_window,
                                    text="Choose your weapon:",
                                    font=('Arial', 16))
        self.instruction_label.pack(padx=20, pady=10)

        self.button_frame_row0 = tk.Frame(self.main_window)
        self.button_frame_row1 = tk.Frame(self.main_window)

        img_rock = PhotoImage(file=os.path.join(IMG_FILES_DIR, 'rock.png'))
        img_paper = PhotoImage(file=os.path.join(IMG_FILES_DIR, 'paper.png'))
        img_scissors = PhotoImage(file=os.path.join(IMG_FILES_DIR, 'scissors.png'))
        img_lizard = PhotoImage(file=os.path.join(IMG_FILES_DIR, 'lizard.png'))
        img_spock = PhotoImage(file=os.path.join(IMG_FILES_DIR, 'spock.png'))

        self.btn_rock = tk.Button(self.button_frame_row0,
                                  text=ROCK, font=('Arial', 18),
                                  command=lambda: self.show_result(ROCK),
                                  image=img_rock, compound=tk.TOP)
        self.btn_rock.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn_paper = tk.Button(self.button_frame_row0,
                                   text=PAPER, font=('Arial', 18),
                                   command=lambda: self.show_result(PAPER),
                                   image=img_paper, compound=tk.TOP)
        self.btn_paper.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn_scissors = tk.Button(self.button_frame_row0,
                                      text=SCISSORS, font=('Arial', 18),
                                      command=lambda: self.show_result(SCISSORS),
                                      image=img_scissors, compound=tk.TOP)
        self.btn_scissors.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.btn_lizard = tk.Button(self.button_frame_row1,
                                    text=LIZARD, font=('Arial', 18),
                                    command=lambda: self.show_result(LIZARD),
                                    image=img_lizard, compound=tk.TOP)
        self.btn_lizard.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn_spock = tk.Button(self.button_frame_row1,
                                   text=SPOCK, font=('Arial', 18),
                                   command=lambda: self.show_result(SPOCK),
                                   image=img_spock, compound=tk.TOP)
        self.btn_spock.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.button_frame_row0.pack(side='top', padx=20, pady=5)
        self.button_frame_row1.pack(side='top', padx=20, pady=5)

        self.main_window.mainloop()

    def show_result(self, player_item: str=None):
        ''' Shows the result on selection / button click.'''
        player_item = player_item.upper()
        machine_item = choice(self.ruleset.get_items())
        winner, action, loser = self.ruleset.get_winner(player_item, machine_item)
        msg_result = f"\nYou choose: {player_item}\nMachine choose: {machine_item}\n\
            \n{winner} {action} {loser}\n"
        if winner == player_item:
            if not messagebox.askyesno(title='You win!', message=f"You have won!\n{msg_result}\n\nWant to play again?"):
                exit()
        elif winner == machine_item:
            if not messagebox.askyesno(title='You lose!', message=f"You have lost!\n{msg_result}\n\nPlay again?"):
                exit()
        else:
            messagebox.showinfo(title='Tie!', message=f"It's a tie!\n\nPlay again!")

if __name__ == '__main__':
    AppGui(Ruleset())