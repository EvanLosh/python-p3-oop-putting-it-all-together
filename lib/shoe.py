#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = ""

    def get_brand(self):
        return self._brand
        
    def set_brand(self, brand):
        self._brand = brand

        
    def get_size(self):
        return self._size
        
    def set_size(self, size):
        is_an_int = isinstance(size, int)
        # print(is_an_int)
        if is_an_int:
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)
    brand = property(get_brand, set_brand)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

# x = Shoe("red", 1.5)
# x.size = 2.5
# print(x.brand)
# print(x.size)