"""#.append(listItem) adds list items
#.remove(listItem) removes list items
#clear(listname) clears the list name"""

list1 = ['Peter','John','Peter','Nick','June','July','August']
list2 = ['Mary','Nida']
list3 = list1.extend(list2) #adds list 2 items to list1 and removes list1
print('List 1 ======>',list1)
print(list1[2:4])
print(list1[-4:-1])
print(list1[3:])
print(list1[:3])

