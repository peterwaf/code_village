"""
This is my story
"""
myStory = """My favourite animal is {animal} and it loves to eat alot of {food}.I have
to import {food} from {city}"""

def tellStory():
    myFavs = dict()
    addFav('animal',myFavs)
    addFav('food',myFavs)
    addFav('city',myFavs)
    story = myStory.format(**myFavs)
    print(story)

def addFav(kavar,myFavs):
    """This allows user input"""
    prompt = 'Enter name of ' +kavar +":"
    response = input(prompt).strip()
    myFavs[kavar] = response

tellStory()
input('Press Enter to exit')