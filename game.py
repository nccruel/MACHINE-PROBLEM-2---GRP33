import pyglet
import time
import engine
from engine import write_to_file,Score,difflevel,get_dictionary,Word,get_dictionary
from pyglet.window import key
from pyglet import clock

gamemode = 0 #different environments/states for the game
words = []  # contains word

#plays background music
player = pyglet.media.Player()
sound = pyglet.media.load('Komiku_-_09_-_Glouglou.wav')
player.queue(sound)
player.play()

window = pyglet.window.Window(width = 1280, height = 720)
sc = Score()
sc.score = 0
type_play = 0
setwords = [' ']
dictionary = get_dictionary()
again = False
tracker = 0
count = 60

welcome = pyglet.text.Label(text = 'Welcome to Typho(o)n!',font_name='Chiller'
               ,font_size=75, bold=True,x = window.width//2, y = 600,anchor_x = 'center', anchor_y = 'center')
play_q = pyglet.text.Label(text = 'Play! (Press 1)',font_name='Chiller'
               ,font_size=40,x = 320, y = 450,anchor_x = 'center', anchor_y = 'center')
play_r = pyglet.text.Label(text = 'Exit! (Press 2)',font_name='Chiller'
               ,font_size=40,x = 960, y = 450,anchor_x = 'center', anchor_y = 'center')
difficulty = pyglet.text.Label(text = 'Choose your game difficulty level:',font_name='Century Gothic'
               ,font_size=36,x = window.width//2, y = 600,anchor_x = 'center', anchor_y = 'center')
diff_options = pyglet.text.Label(text = '1 (Easy) | 2 (Moderate) | 3 (Difficult)' ,font_name='Century Gothic'
               ,font_size=36,x = window.width//2, y = 550,anchor_x = 'center', anchor_y = 'center')
output = pyglet.text.Label('', font_name='Century Gothic', font_size=45, bold=True, italic=True, color = (0, 255, 0, 255),
                          x=window.width//2, y=40,
                          anchor_x='center', anchor_y='center')
inp = pyglet.text.Label('', font_name='Century Gothic', font_size=45, bold=True, italic=True, color = (255, 0, 0, 0),
                          x=window.width//2, y=40,
                          anchor_x='center', anchor_y='center')
score_out = pyglet.text.Label("Score: 0", font_name='Century Gothic', font_size=28, color=(0, 255, 255, 255),
                          x=100, y=700,
                          anchor_x='center', anchor_y='center')

timer = pyglet.text.Label("00:" + str(count), font_name = 'Century Gothic', font_size=34, color=(0, 255, 0, 255),
                          x=1200, y=700,
                          anchor_x='center', anchor_y='center')

tryagain = pyglet.text.Label(text = 'Try again?',font_name='Rockwell'
               ,font_size=36,x = window.width//2, y = 500,anchor_x = 'center', anchor_y = 'center')
ta_y = pyglet.text.Label(text = 'Yes! (Press y)',font_name='Rockwell'
               ,font_size=36,x = 320, y = 300,anchor_x = 'center', anchor_y = 'center')
ta_n = pyglet.text.Label(text = 'No! (Press n)',font_name='Rockwell'
               ,font_size=36,x = 960, y = 300,anchor_x = 'center', anchor_y = 'center')
gameover = pyglet.text.Label(text = 'GAME OVER!',font_name='Rockwell'
               ,font_size=60, color=(255, 0, 0, 255), x = window.width//2, y = 500,anchor_x = 'center', anchor_y = 'center')
final_score =  pyglet.text.Label("Total Score: ", font_name='Century Gothic', font_size=45, color=(0, 255, 255, 255),
                          x=window.width//2, y=385,
                          anchor_x='center', anchor_y='center')  
leaderboard = pyglet.text.Label('Enter your name:',font_name='Century Gothic'
            ,font_size=36,x = 640, y = 100,anchor_x = 'center', anchor_y = 'center')    
timeup = pyglet.text.Label(text = "TIME'S UP!",font_name='Rockwell'
               ,font_size=60, color=(255, 0, 0, 255), x = window.width//2, y = 600,anchor_x = 'center', anchor_y = 'center')

@window.event
def on_key_press(symbol, modifiers):
      global gamemode, again, setwords, count, tracker

      if gamemode == 0:       # main-menu input
            if symbol == key._1: # [Backspace]
                  gamemode = 1
            elif symbol == key._2:
                  exit()
      elif gamemode == 1: #difficulty level
            if symbol == key._1:
                  gamemode = 2
                  setwords = difflevel(3,6,dictionary)
            elif symbol == key._2:
                  gamemode = 2
                  setwords = difflevel(7,9,dictionary)
            elif symbol == key._3:
                  gamemode = 2
                  setwords = difflevel(10,16,dictionary)
            words.clear()
            count = 60
            if count < 0:
              output.text = ''
              gamemode = 4
            
            

      elif gamemode == 2:     # In-Game Input
            if symbol == key.BACKSPACE: # [Backspace]
                  output.text = output.text[:-1] # Delete one letter from screen
            elif symbol == key.ENTER:
                  check_input()
                  score_out.text = "Score: " + str(sc.score)
                  final_score.text = "Total Score: " + str(sc.score)
                  output.text = ''
            else:
                  output.text += chr(symbol)
                  
      elif gamemode == 3 or gamemode == 4: #Game Over or Time's Up
            if again == False:
                    if symbol == key.BACKSPACE: # [Backspace]
                          output.text = output.text[:-1] # Delete one letter from screen      
                    elif symbol == key.ENTER:
                          player_name = output.text
                          tracker = 1
                          again = True
                          write_to_file(player_name, sc.score)
                          output.text = ''


                    else:
                          output.text += chr(symbol)
            
            elif again == True:
                  window.clear()
                  if symbol == key.Y:
                        sc.score = 0
                        score_out.text = "Score: " + str(sc.score)
                        final_score.text = "Total Score: " + str(sc.score)
                        output.text = ''
                        tracker = 0
                        again = False
                        gamemode = 0

                  elif symbol == key.N:
                        exit()


def draw():
      global gamemode, tracker
      if gamemode == 0:
            window.clear()       #draw main-menu
            welcome.draw()
            play_q.draw()
            play_r.draw()
         
      elif gamemode == 1:       #draw difficulty
            difficulty.draw()
            diff_options.draw()

      elif gamemode == 2:      #draw in-game environment
            for word in words:
                  word.draw_self()
                  if word.check == 1:
                        output.text = ''
                        gamemode = 3
                        break       
            score_out.draw()
            output.draw() 
            timer.draw()
      elif gamemode == 3: #game over environment (when a word falls)
            window.clear()
            gameover.draw()
            final_score.draw()
            leaderboard.draw()
            output.draw()
            if again == True:
                  window.clear()
                  tryagain.draw()
                  ta_y.draw()
                  ta_n.draw()
      elif gamemode == 4: #time's up environment
            window.clear()
            timeup.draw()
            final_score.draw()
            leaderboard.draw()
            output.draw()
            if again == True and tracker == 1:
                  window.clear()
                  tryagain.draw()
                  ta_y.draw()
                  ta_n.draw()
def check_input():  #checks input of user
      for word in words:
            if word.display.text == output.text:
                  words.remove(word)
                  sc.score += len(output.text)
        
def create_blocks(time):  # instantiate words
      words.append(Word(setwords))
                        
@window.event
def on_draw():
      window.clear()
      draw()

def update(t): #handles decrementing the timer
      global count, gamemode, tracker, again
      count-=1
      if count > 0:
            if count < 11:
                  timer.color = (255,0,0,255)
                  timer.text = "00:"+ str(count).zfill(2)
            else:
                  timer.text = "00:"+ str(count).zfill(2)
      else:
        gamemode = 4            

clock.schedule_interval(create_blocks, 2)
clock.schedule_interval(update, 1)

pyglet.app.run()
