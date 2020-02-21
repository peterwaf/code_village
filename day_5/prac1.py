a = 5
b = 10
print('{}+{}={}'.format(a,b,a+b))



countries = dict()
countries['Kenya'] = 'Nairobi'
countries['Uganda'] = 'Kampala'

output = '{Kenya} {Uganda}'.format(**countries)
print(output)
