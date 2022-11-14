"""
This file contains common functions and variables
for the game, such as basic mathematical calculations
as well as variables.
"""

COLOURS = (
    BLACK := (0, 0, 0),
    GRAY := (127, 127, 127),
    WHITE := (255, 255, 255),
    RED := (255, 0, 0),
    GREEN := (0, 255, 0),
    BLUE := (0, 0, 255),
    YELLOW := (255, 255, 0),
    CYAN := (0, 255, 255),
    MAGENTA := (255, 0, 255),
)

class CoordinateTransformer:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def screen_cartesian_transform(self, p, q):
        return p, q - self.height