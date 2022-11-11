# Imports
import os, sys          # Generic standard libraries

import pygame           # Pygame for graphics

import utils            # Utils module with common variables and functions
from balls import Ball  # Ball class

class Game:
    """
    Main Game class for game logic and playing
    """
    def __init__(self):
        """
        Initialise instance of main game class
        """
        # Window size of 480p
        self.WIN_WIDTH = 854
        self.WIN_HEIGHT = 480
        self.DIMENSIONS = (self.WIN_WIDTH, self.WIN_HEIGHT)
        pygame.init()                   
        self.WIN = pygame.display.set_mode(self.DIMENSIONS, vsync=1)

        self.running = True
        self.main()

    def main(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    Game()