import pygame
import variables


class GameMain:
    running = True
    surface = pygame.surface.Surface
    counter = 0

    def game_loop(self):
        item1 = pygame.Rect(variables.rectangle_definition)
        pygame.draw.rect(self.surface, variables.COLOURS.GREEN.value, item1)
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