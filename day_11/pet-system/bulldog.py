from dog import Dog
class Bulldog(Dog):
    def __init__(self,color,name,age,sound,food,size): #adding extra properties
        super().__init__(color,name,age,sound,food) #just a statement , not a function
        self.size = size
            
    
    
    def walk(self,walkingStyle):
        self.walkingStyle = walkingStyle
        print('Bulldog  walks like a {} '.format(self.walkingStyle))