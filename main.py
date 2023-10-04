import numpy as np
from PIL import Image

class Canvas:
    """Obj where all shapes will be drawn"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #Change [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

class Rectangle:
    """A rectangle shape that can be drawn on a Canvas obj"""
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Drawn itself into the canvas"""
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    """A square shape that can be drawn on a Canvas obj"""
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Drawn itself into the canvas"""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color

canvas = Canvas(100, 80, color=(255, 255, 255))
r1 = Rectangle(20, 40, 10, 20, color=(110, 140, 120))
r1.draw(canvas)
s1 = Square(20, 20, 10, color=(10, 80, 100))
s1.draw(canvas)
canvas.make('canvas.png')