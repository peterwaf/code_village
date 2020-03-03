class Pets:
    dogs = []
    
    def __init__(self,dogs):
        self.dogs = dogs
        
class Dog:
    def __init__(self,color,name,age,sound,food):
        self.color = color
        self.name = name
        self.age = age
        self.sound = sound
        self.food = food
        
    def bark(self):
        print('The {} {}'.format(self.name,self.sound))
        
    def eat(self):
        print('The {} eats {}'.format(self.name,self.food))
        
    def age(self):
        print('{} is {} years old '.format(self.name,self.age))

class Germanshep(Dog):
    
    def sleep(self):
        print('German sleeps like a carmel ')
        
class Bulldog(Dog):
    
    def walk(self,walkingStyle):
        self.walkingStyle = walkingStyle
        print('Bulldog  walks like a {} '.format(self.walkingStyle))
        
class Jackal(Dog):
    
    def dance(self,danceStyle):
        self.danceStyle = danceStyle
        print('Jackal dances like {}'.format(danceStyle))

germanShepheded = Germanshep('Red','Tom',5,'Wooh','Bigbones')
germanShepheded.bark()
germanShepheded.sleep()
bullDog = Bulldog('Green','Scooby',8,'Whoogrrrr','Goat Bones')
print(bullDog.name)
bullDog.walk('Tiktak')
jackal = Jackal('Grey','Mr Nice',3,'Whu whu','Zebra Bones')
jackal.bark()
jackal.dance('Wild dance dance')

mydog_list = [germanShepheded,bullDog,jackal]
Pets.dogs = mydog_list
print('=== My pets are ====')
for dog in Pets.dogs:
    print('Name :',dog.name,'age :',dog.age,'Food :',dog.food)