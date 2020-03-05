from dog import Dog
class Jackal(Dog):
    
    def dance(self,danceStyle):
        self.danceStyle = danceStyle
        print('Jackal dances {}'.format(danceStyle))