'''
  This is A BASE class for the entire project
'''

class Base:
    '''
        This is a base class which will define every class in the project
    '''
    def __init__(self, id=None):
        self.__nb_objects = 0
        
        if self.id != None :
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
