class_scores = {'0101': {'Name': 'mathew', 'Class': '1', 'scores': {'english': 45, 'maths': 98}}, '4875': {'Name': 'john', 'Class': '1', 'scores': {'geography': 56}}}
allStudentScores = 0
allStudentScoresCounter = 0
for a,y in class_scores.items():
    print(y['scores'])
    allStudentScoresCounter += len(y['scores'])
    for k,v in y['scores'].items():
        allStudentScores += v
print(allStudentScores)
print(allStudentScoresCounter)