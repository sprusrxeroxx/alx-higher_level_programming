#!/usr/bin/python3

# This is A BASE class for the entire project


class Base:
#This is a base class which will define every class in the project

    __nb_objects = 0
    def __init__(self, id=None):
        
        if id != None :
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
