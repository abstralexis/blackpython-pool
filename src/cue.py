import math

import pygame

from utils import *
import time
from balls import Ball

def blitRotateCenter(surf, image, topleft, angle):

    """
    Thanks to Rabbid76 on StackOverflow
    """

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

class Cue:
    def __init__(self, x: float, y: float, cue_ball: Ball, screen: pygame.display):
        self.size = (250, 250)
        self.image = pygame.image.load("..\\assets\\cue-centred.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.angle = 0#deg
        self.focusangle = 0#deg
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(self.x, self.y, self.size[0], self.size[1])
        self.cue_ball = cue_ball
        self.aoff = 45
        self.power = 1
        self.screen = screen
        self.hide = False

    def focus(self, screen: pygame.display):
        # Set tip to centre of the ball focused
        self.rect.center = (self.cue_ball.centrex, self.cue_ball.centrey)

        # Get the mouse pos
        (mousex, mousey) = pygame.mouse.get_pos()

        # Get angle between mouse and pivot point (top left)
        self.dx = self.cue_ball.centrex - mousex
        self.dy = self.cue_ball.centrey - mousey
        self.angle = math.degrees(-math.atan2(self.dy, self.dx))
        self.focusangle = self.angle + self.aoff

    def draw(self):
        if not self.hide:
            self.rect.center = (self.cue_ball.centrex, self.cue_ball.centrey)
            blitRotateCenter(
                self.screen, 
                self.image, 
                (
                    self.cue_ball.centrex - (self.size[0] / 2),
                    self.cue_ball.centrey - (self.size[1] / 2)
                ), 
                self.focusangle)

    # def shot_animation(self):
    #     xmult = 1 if self.x <= self.cue_ball.centrex else -1
    #     ymult = 1 if self.y <= self.cue_ball.centrey else -1
    #     gradient = self.dy // self.dx
    #     distance = 10
    #     # Move back slowly along line
    #     for _ in range(distance):
    #         self.rect.center = (
    #             self.cue_ball.centrex + (1*xmult),
    #             self.cue_ball.centrey + (gradient*ymult)
    #         )
    #         blitRotateCenter(
    #             self.screen,
    #             self.image,
    #             (
    #                 self.rect.center[0] - (self.size[0]/2),
    #                 self.rect.center[1] - (self.size[1]/2)
    #             ),
    #             self.focusangle
    #         )
    #         time.sleep(0.05)
    #     # Move forward quickly along line
    #     return