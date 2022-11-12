import pygame

class Ball:
    def __init__(self, x, y, radius):
        """
        Takes some arguments and calculates the others
        """
        # Arguments
        self.centrex = x                # Centre x coordinate
        self.centrey = y                # Centre y coordinate
        self.radius = radius            # Radius
        self.colour = (0, 0, 0)         # RGB colour tuple

        # Calculated
        self.width = self.radius * 2              # Rect width
        self.height = self.radius * 2             # Rect height
        self.left = self.centrex - self.radius    # Top left y coordinate
        self.top = self.centrey - self.radius     # Top left x coordinate
        self.rect = pygame.rect.Rect(
            self.left, 
            self.top, 
            self.width, 
            self.height
        )   # Pygame rect

        # Consts
        self.MASS = 0.16#kg             # mass var for F = ma calculations

    def draw(self, screen: pygame.display):
        self.rect = pygame.rect.Rect(
            self.left, 
            self.top, 
            self.width, 
            self.height
        )
        pygame.draw.circle(
            screen,
            self.colour, 
            (self.centrex, self.centrey), 
            self.radius
        )