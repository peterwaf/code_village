a = 5
b = 10
print('{}+{}={}'.format(a,b,a+b))



countries = dict()
countries['Kenya'] = 'Nairobi'
countries['Uganda'] = 'Kampala'

output = '{Kenya} {Uganda}'.format(**countries)
print(output)

"""
Assignment
==========================
1 user enters multiple subjects + scores
2 option to end
3 output
-subject
-grade
-mean grade

"""

all_scores = dict()
all_scores[subjectName] = subjectScore
print(all_scores)