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

        self.main_window = AppWindow("RPSLS", 680, 440)

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

        self.btn_rock = WeaponButton(self.button_frame_row0, ROCK, img_rock, self.show_result)
        self.btn_rock.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn_paper = WeaponButton(self.button_frame_row0, PAPER, img_paper, self.show_result)
        self.btn_paper.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn_scissors = WeaponButton(self.button_frame_row0, SCISSORS, img_scissors, self.show_result)
        self.btn_scissors.grid(row=0, column=2, sticky=tk.W+tk.E)

        self.btn_lizard = WeaponButton(self.button_frame_row1, LIZARD, img_lizard, self.show_result)
        self.btn_lizard.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn_spock = WeaponButton(self.button_frame_row1, SPOCK, img_spock, self.show_result)
        self.btn_spock.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.button_frame_row0.pack(side='top', padx=20, pady=5)
        self.button_frame_row1.pack(side='top', padx=20, pady=5)

        self.main_window.mainloop()

    def show_result(self, player_item: str = None):
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
            messagebox.showinfo(title='Tie!', message="It's a tie!\n\nPlay again!")


class AppWindow(tk.Tk):
    def __init__(self, title, res_x, res_y, center=True) -> None:
        super().__init__()
        self.title(title)
        if center:
            center_x = int((self.winfo_screenwidth() / 2) - (res_x / 2))
            center_y = int((self.winfo_screenheight() / 2) - (res_y / 2))
            self.geometry(f"{res_x}x{res_y}+{center_x}+{center_y}")
        else:
            self.geometry(f"{res_x}x{res_y}")


class WeaponButton(tk.Button):
    def __init__(self, master, btn_name: str, btn_img, btn_cmd) -> None:
        super().__init__(master=master,
                         text=btn_name.capitalize(),
                         font=('Arial', 18),
                         command=lambda: btn_cmd(btn_name),
                         image=btn_img,
                         compound=tk.TOP)


if __name__ == '__main__':
    AppGui(Ruleset())
