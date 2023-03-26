import pygame
import variables
from pygame import rect
import game.food as food


class GameMain:
    running = True
    surface = pygame.surface.Surface
    counter = 0

    food1 = food.Food(countdown_start=10)
    food1.change_food_location(35, 150)


    item1 = rect.Rect(10, 10, 25, 25)
    item2 = rect.Rect(20, 20, 25, 25)
    item3 = rect.Rect(30, 30, 25, 25)
    f = [item1, item2, item3]

    def game_loop(self):
        for item in self.f:
            pygame.draw.rect(self.surface, variables.COLOURS.GREEN.value, item)

        pygame.draw.rect(self.surface, variables.COLOURS.GREEN.value, self.food1.food_display)
        # pygame.draw.rect(self.surface, variables.COLOURS.GREEN.value, item1)
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((880, 495))
        pygame.display.set_caption("What's In My Freezer?")

        self.game_loop()

# https://www.geeksforgeeks.org/how-to-set-up-the-game-loop-in-pyggame/