"""function that returns true if 007 in order"""
class Dog:
    species = 'mamals'
    
    def __init__(self,breed,name,spots):
        self.breed =  breed
        self.name = name
        self.spots = spots
        
    def bark(self,number):
        print('Woof ! my name is {} and I bark {} times'.format(self.name,number))

max = Dog('German Shephered','Maxi','DOtted')
print(max.bark(5))
