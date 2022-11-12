import math

import pygame

import utils
from balls import Ball


def blitRotate2(surf: pygame.display, image: pygame.surface, topleft, angle):
    """
    https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/
    master/examples/surface_rotate/pygame_image_rotate_5_pivot_function.py
    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)

class Cue:
    def __init__(self, x: float, y: float):
        size = (200, 200)
        self.image = pygame.image.load("..\\assets\\cue.png")
        self.image = pygame.transform.scale(self.image, size)
        self.angle = 0#deg
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, size[0], size[1])

    #TODO Fix
    def focus(self, screen: pygame.display, cue_ball: Ball):
        # Set top left (tip) to centre of the ball focused
        self.x = cue_ball.centrex
        self.y = cue_ball.centrey

        # Get the mouse pos
        (mousex, mousey) = pygame.mouse.get_pos()

        # Get angle between mouse and pivot point (top left)
        dx = abs(cue_ball.centrex - mousex)
        dy = abs(cue_ball.centrey - mousey)
        self.angle = math.degrees(math.atan2(dy, dx))
        blitRotate2(screen, self.image, (self.x, self.y), self.angle)

    def draw(self, screen: pygame.display):
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        pygame.Surface.blit(screen, self.image, self.rect)