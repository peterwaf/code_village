student_details = {'0101': {'Name': 'john', 'Class': '1', 'scores': {'maths': 98, 'english': 65}}, '0202': {'Name': 'peter', 'Class': '1', 'scores': {'geography': 90}}}
for x,y in student_details.items():
    print(y.get("Name"))
    print(y.get("Class"))
    #print(y.get("scores"))
    for k,v in y.get("scores").items():
        print(k,":",v)
