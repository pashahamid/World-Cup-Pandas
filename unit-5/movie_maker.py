'''
import json
class Movie:
    def __init__(self,title,genre,running_time):
        self.title = title
        self.genre = genre
        self.running_time = running_time
        self.cast = []

    def add_cast(self, actor):

        
        #expect actor to be
        {
            name:
            age:
            sex:
        }
                    
        if 'name' in 'actor' and 'age' in actor and 'sex' in actor:
            self.cast.append(actor)
        else:
            print('Actor has incomplete data')

    def save_to_file(self, file):
        with open(file, 'w') as outfile:
            json.dump(vars(self), outfile)

m = Movie('The Avengers', 'Sci Fi/Fantasy/Superhero', 2.5)

m.add_cast({'name': 'RDJ', 'age': 45, 'sex': 'M'})
m.add_cast({'name' : 'Scarlet Johanson'})

m.save_to_file('movie.josn')

print(vars(m))

