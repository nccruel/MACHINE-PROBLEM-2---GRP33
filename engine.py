import pyglet
import random as r
from pyglet import clock

# engine

""" Functions """
def get_dictionary():  # load dictionary and filter based on requirements
	file = open("newdic.txt")
	dictionary = []
	for word in file:
		dictionary.append(word.rstrip())
	return dictionary

def check_input(input1):  # check if input of user is present in the screen
	for word in words:
		if word.display.text == input1:
			words.remove(word)   #remove word from screen
			score += 1   #update score
			
def difflevel(m, n, dicti):
	l_words = []
	for w in dicti:
		if len(w) in range(m, n+1):
			l_words.append(w)
	return l_words

def write_to_file(name,score):
	file = open('leaderboard.txt','a')
	file.write('\n')
	file.write('\t'+ name +' ------ '+str(score)+' pts')

""" Classes """
class Word():  # blueprint for block of words
	def __init__(self,wordset):
		fonts = ['Arial', 'Century Gothic', 'Calibri', 'Comic Sans MS', 'Berlin Sans FB', 'Brittanic Bold', 'MV Boli', 'Tahoma', 'Verdana', 'Footlight MT Light', 'Bauhaus 93', 'Courier New']
		self.display = pyglet.text.Label(r.choice(wordset),font_name=fonts[r.randint(0, len(fonts)-1)]
				,font_size=r.randint(30,40),bold=True,x = r.randint(50, 950), y = 700)
		self.check = 0
		def update_self(dt):
			if self.display.y < 45:
				self.check = 1
			else:
				self.display.y -= 1
		clock.schedule_interval(update_self,1/100)

	def draw_self(self):
		self.display.draw()

class Score():
		def __init__(self):
				self.score = 0
