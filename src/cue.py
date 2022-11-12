import math

import pygame

import utils
from balls import Ball


def blitRotateCenter(surf, image, topleft, angle):

    """
    Thanks to Rabbid76 on StackOverflow
    """

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

class Cue:
    def __init__(self, x: float, y: float, cue_ball: Ball):
        self.size = (200, 200)
        self.image = pygame.image.load("..\\assets\\cue-centred.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.angle = 0#deg
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, self.size[0], self.size[1])
        self.cue_ball = cue_ball

    #TODO Fix
    def focus(self, screen: pygame.display):
        # Set tip to centre of the ball focused
        self.rect.center = (self.cue_ball.centrex, self.cue_ball.centrey)

        # Get the mouse pos
        (mousex, mousey) = pygame.mouse.get_pos()

        # Get angle between mouse and pivot point (top left)
        dx = self.cue_ball.centrex - mousex
        dy = self.cue_ball.centrey - mousey
        self.angle = math.degrees(math.atan2(dx, dy))

    def draw(self, screen: pygame.display):
        self.rect.center = (self.cue_ball.centrex, self.cue_ball.centrey)
        blitRotateCenter(
            screen, 
            self.image, 
            (
                self.cue_ball.centrex - (self.size[0] / 2),
                self.cue_ball.centrey - (self.size[1] / 2)
            ), 
            self.angle)