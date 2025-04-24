# Name: Vlad Snopko
# Date: March 23, 2025
# Description:
# This program is about a flower class using Python's object-oriented programming.
# The class has one attribute (name) and two methods (grow and bloom).
# I added one more flower to practice creating and using objects.

class Flower:  # This defines a class called Flower
    def __init__(self, name):  # This method runs when a new flower object is made
        self.name = name  # This saves the flower name as an attribute

    def grow(self):  # This method prints a message that the flower is growing
        print("The " + self.name + " is growing.")

    def bloom(self):  # This method prints a message that the flower is blooming
        print("The " + self.name + " is blooming.")

def main():
    flower1 = Flower("Rose")  # First flower object with name Rose
    flower1.grow()
    flower1.bloom()

    flower2 = Flower("Daisy")  # Second flower object with name Daisy
    flower2.grow()
    flower2.bloom()

    flower3 = Flower("Sunflower")  # Third flower I added myself
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":  # This makes sure main runs only when this file is run
    main()