#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = "Adidas", size = 9):
        self.brand = brand
        self.size = size
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            self._size = "not an integer"
            print("size must be an integer")
        else:
            self._size = size
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
