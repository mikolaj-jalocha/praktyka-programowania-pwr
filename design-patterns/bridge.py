from abc import ABC, abstractmethod

import numpy as np
import time
import os


class Color(ABC):
    @abstractmethod
    def pokoloruj(self) -> str:
        pass

class RedColor(Color):
    def pokoloruj(self) -> str:
        return "czerwony"

class BlueColor(Color):
    def pokoloruj(self) -> str:
        return "niebieski"

class Shape:

    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def show(self):
        pass

class Rectangle(Shape):

    def show(self):
        print("Tu narysuje prostokat w kolorze: {self.color.pokoloruj()}")


class Triangle(Shape):

    def show(self):
        print("Tu narysuje trojkat w kolorze: {self.color.pokoloruj()}")

def main():
    red = RedColor()
    blue = BlueColor()

    red_rectangle = Rectangle(red)
    blue_triangle = Triangle(blue)


    blue_triangle.show()


if __name__ == "__main__":
    main()
