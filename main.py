# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import variables
import pygame
import game.game_main

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {variables.COLOURS.RED.value}')  # Press Ctrl+F8 to toggle the breakpoint.

def main():
    new_game = game.game_main.Main()
    new_game.game_loop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
