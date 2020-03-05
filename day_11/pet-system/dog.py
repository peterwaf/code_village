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