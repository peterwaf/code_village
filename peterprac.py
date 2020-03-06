class Car:
    allcars = []
    numOfLegs = 4
    def __init__(self,name,model,year,color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        
        
    def getDetails(self):
        print('The name of the car is {}'.format(self.name))
        print('The name of the car is {}'.format(self.model))
        print('The name of the car is {}'.format(self.year))
        print('The name of the car is {}'.format(self.color))

class Toyota(Car):
    def __init__(self,name,model,year,color,owners):
        super().__init__(name,model,year,color)
        self.owners = owners
        
    def getOwner(self):
        print('The owner is called {} '.format(self.owners))
        
mytoyota = Toyota('Toyota','Corolla',2008,'red','Peter')
teachertoyota = Toyota('Toyota','Auris',2020,'Grey','Stanley')
mytoyota.getDetails()
mytoyota.getOwner()
teachertoyota.getDetails()
teachertoyota.getOwner()
listofcars = []
listofcars.append(mytoyota)
listofcars.append(teachertoyota)
