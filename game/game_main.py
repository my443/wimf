import pygame

class GameMain:
    running = True
    counter = 0

    def game_loop(self):
        while self.running:
            print("something", self.counter)

            self.counter += 1

            if self.counter == 10:
                self.running = False

    def __init__(self):
        pygame.init()
        self.game_loop()

# https://www.geeksforgeeks.org/how-to-set-up-the-game-loop-in-pyggame/