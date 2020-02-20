radius = int(input('Enter the radius :'))
the_option = input('Type a for area or c for circumfrence :')
PI = 3.142
def area(radius):
    radius_square = radius * radius
    result = PI*radius_square
    print('The area is {}'.format(result))
    
def circumfrence(radius):
    circumfrence = 2 * PI * radius
    print('The circumfrence is {}'.format(circumfrence))
        
if (the_option =='a'):
    area(radius)
    
elif (the_option =='c'):
    circumfrence(radius)
else:
    print('Invalid input')


