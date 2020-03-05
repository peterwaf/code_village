from pet import Pets
from dog import Dog
from germanshep import Germanshep
from bulldog import Bulldog
from jackal import Jackal

#german shephered

germanShepheded = Germanshep('Red','Tom',5,'Wooh','Bigbones')
germanShepheded.bark()
germanShepheded.sleep()

#bulldog

bullDog = Bulldog('Green','Scooby',8,'Whoogrrrr','Goat Bones',8)
print('Number of pupies for bulldog :',bullDog.size)
print('The bulldog\'s name is',bullDog.name)
bullDog.walk('Tiktak')

#jackal

jackal = Jackal('Grey','Mr Nice',3,'Whu whu','Zebra Bones')
jackal.bark()
jackal.dance('Wild dance dance')

#all pets list

mydog_list = [germanShepheded,bullDog,jackal]
Pets.dogs = mydog_list
print('=== My pets are ====')
for dog in Pets.dogs:
    print('Name :',dog.name,'age :',dog.age,'Food :',dog.food)
    
print('====')


