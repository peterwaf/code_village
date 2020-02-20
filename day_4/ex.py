radius = int(input('Enter the radius :'))

PI = 3.142
def area(radius):
    area = PI*radius*radius
    return area
   
    
def circumfrence(radius):
    circumfrence = 2 * PI * radius
    return circumfrence
    
    
print('area is {} circumfrence is {}'.format(area(radius),circumfrence(radius)))



