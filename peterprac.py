"""function that returns true if 007 in order"""
class Dog:
    """a simple attempt to crate a dog model"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print('The {} is now sitting'.format(self.name))
    
    def rollOver(self):
        print('The {} is now rolling over'.format(self.name))

jack = Dog('Jack',18)
jack.sit()