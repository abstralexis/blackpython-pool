from dataclasses import dataclass
import pygame

@dataclass
class Ball:
    """
    Takes some arguments and calculates the others
    """
    # Arguments
    centrex: int                    # Centre x coordinate
    centrey: int                    # Centre y coordinate
    radius: int                     # Radius
    colour = (0, 0, 0)              # RGB colour tuple

    # Calculated
    width = radius * 2              # Rect width
    height = radius * 2             # Rect height
    left = centrex - radius         # Top left y coordinate
    top = centrey - radius          # Top left x coordinate
    rect = pygame.rect.Rect(left, top, width, height)   # Pygame rect

    # Consts
    MASS = 0.16#kg                  # mass var for F = ma calculations