# created 09/04/2014
# by Vittorio Cuculo

import pygame, sys
import time
import datetime
from pygame.locals import *
import locale
import serial

locale.setlocale(locale.LC_TIME, '')

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('KIND')
pygame.display.toggle_fullscreen();
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)

# define fonts used
fontSkinny70 = pygame.font.Font('Bullet.ttf', 70)
fontSkinny90 = pygame.font.Font('Bullet.ttf', 90)
fontSkinny150 = pygame.font.Font('Bullet.ttf', 150)

ser = serial.Serial('/dev/ttyACM0', 9600)

locked = True
weight = 0
state = 0
tara = 0
hours = 0
minutes = 0
seconds = 0
milliseconds = 0
recipeStep = 0

def standby():
  global locked
  sunImg = pygame.image.load('sun.png')
  keyImg = pygame.image.load('key.png')

  timeObj = fontSkinny90.render(time.strftime("%H:%M:%S"), True, BLACK, WHITE)
  timeRectObj = timeObj.get_rect()
  timeRectObj.center = (400, 100)

  textSurfaceObj = fontSkinny150.render('BUONGIORNO', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (400, 300)

  dateObj = fontSkinny90.render(time.strftime("%a %d %B"), True, BLACK, WHITE)
  dateRectObj = dateObj.get_rect()
  dateRectObj.center = (400, 500) 

  tempObj = fontSkinny90.render(u"20°C", True, BLACK, WHITE)
  tempRectObj = tempObj.get_rect()
  tempRectObj.center = (730, 560) 

  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  DISPLAYSURF.blit(timeObj, timeRectObj)
  DISPLAYSURF.blit(dateObj, dateRectObj)
  DISPLAYSURF.blit(tempObj, tempRectObj)
  DISPLAYSURF.blit(sunImg, (620, -15))
  if (locked):
    DISPLAYSURF.blit(keyImg, (10, 20))


def scale(weight=-1):
  global tara
  print([weight, tara])

  if(weight > -1):
    weight = weight-tara
    textSurfaceObj = fontSkinny150.render(str(weight), True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 300)
    text2SurfaceObj = fontSkinny90.render('gr', True, BLACK, WHITE)
    text2RectObj = text2SurfaceObj.get_rect()
    text2RectObj.center = (700, 300)
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)

def recipe():
  global recipeStep

  if (recipeStep == 0):
    emptyImg = pygame.image.load('empty.png')
    fullImg = pygame.image.load('full.png')

    textSurfaceObj = fontSkinny90.render('Tiramisu', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 100)

    text1SurfaceObj = fontSkinny90.render('Pizza', True, GREY, WHITE)
    text1RectObj = text1SurfaceObj.get_rect()
    text1RectObj.center = (400, 200)

    text2SurfaceObj = fontSkinny90.render('Canederli', True, GREY, WHITE)
    text2RectObj = text2SurfaceObj.get_rect()
    text2RectObj.center = (400, 300)

    text3SurfaceObj = fontSkinny90.render('Cous cous', True, GREY, WHITE)
    text3RectObj = text3SurfaceObj.get_rect()
    text3RectObj.center = (400, 400)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
    DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
    DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)

    DISPLAYSURF.blit(fullImg, (80, 70))
    DISPLAYSURF.blit(emptyImg, (80, 170))
    DISPLAYSURF.blit(emptyImg, (80, 270))
    DISPLAYSURF.blit(emptyImg, (80, 370))

  elif (recipeStep == 1):
    textSurfaceObj = fontSkinny150.render('Tiramisu', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 300)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    recipeStep += 1
    time.sleep(2)

  elif (recipeStep == 2):
    textSurfaceObj = fontSkinny90.render('Ingredienti', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 80)

    text1SurfaceObj = fontSkinny70.render('120 gr Zucchero', True, BLACK, WHITE)
    text1RectObj = text1SurfaceObj.get_rect()
    text1RectObj.center = (400, 190)

    text2SurfaceObj = fontSkinny70.render('6 Uova', True, BLACK, WHITE)
    text2RectObj = text2SurfaceObj.get_rect()
    text2RectObj.center = (400, 260)

    text3SurfaceObj = fontSkinny70.render('500 gr Mascarpone', True, BLACK, WHITE)
    text3RectObj = text3SurfaceObj.get_rect()
    text3RectObj.center = (400, 330)

    text4SurfaceObj = fontSkinny70.render('Q.B. Cacao in polvere', True, BLACK, WHITE)
    text4RectObj = text4SurfaceObj.get_rect()
    text4RectObj.center = (400, 400)

    text5SurfaceObj = fontSkinny70.render('Q.B. Caffe\'', True, BLACK, WHITE)
    text5RectObj = text5SurfaceObj.get_rect()
    text5RectObj.center = (400, 470)

    text6SurfaceObj = fontSkinny70.render('400 gr Savoiardi', True, BLACK, WHITE)
    text6RectObj = text6SurfaceObj.get_rect()
    text6RectObj.center = (400, 530)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(text1SurfaceObj, text1RectObj)
    DISPLAYSURF.blit(text2SurfaceObj, text2RectObj)
    DISPLAYSURF.blit(text3SurfaceObj, text3RectObj)
    DISPLAYSURF.blit(text4SurfaceObj, text4RectObj)
    DISPLAYSURF.blit(text5SurfaceObj, text5RectObj)
    DISPLAYSURF.blit(text6SurfaceObj, text6RectObj)

  elif (recipeStep == 3):
    textSurfaceObj = fontSkinny150.render('INIZIAMO!', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 300)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    recipeStep += 1
    time.sleep(2)

  elif (recipeStep == 4):
    textSurfaceObj = fontSkinny70.render('Appoggia il contenitore', True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (400, 300)

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    pygame.display.update()

def timer():
  global hours, minutes, seconds, milliseconds, clock
  if milliseconds > 1000:
    seconds += 1
    milliseconds -= 1000
  if seconds > 60:
    minutes += 1
    seconds -= 60
  if minutes > 60:
    hours += 1
    minutes -= 60

  milliseconds += clock.tick_busy_loop(60)
  textSurfaceObj = fontSkinny150.render("{:0>2d}:{:0>2d}:{:0>2d}".format(hours, minutes, seconds), True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (400, 300)

  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)


def resetTimer():
  global clock, hours, minutes, seconds, milliseconds
  clock = pygame.time.Clock()
  hours = 0
  minutes = 0
  seconds = 0
  milliseconds = 0

def startScale(weight):
  global tara
  tara = weight
  scaleImg = pygame.image.load('scale.png')
  textSurfaceObj = fontSkinny150.render('BILANCIA', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (400, 300)
  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(scaleImg, (-50, 30))
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  pygame.display.update()
  time.sleep(2)

def startTimer():
  scaleImg = pygame.image.load('timer.png')
  textSurfaceObj = fontSkinny150.render('TIMER', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (400, 300)
  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(scaleImg, (-50, 30))
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  pygame.display.update()
  time.sleep(2)
  resetTimer()

def startRecipe():
  scaleImg = pygame.image.load('recipe.png')
  textSurfaceObj = fontSkinny150.render('CUCINIAMO!', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (400, 300)
  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(scaleImg, (-50, 30))
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  pygame.display.update()
  time.sleep(2)
  resetTimer()

def turnOn():
  textSurfaceObj = fontSkinny150.render('SONO PRONTO!', True, BLACK, WHITE)
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (400, 300)

  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(textSurfaceObj, textRectObj)
  pygame.display.update()
  time.sleep(1)

def readSerial():
  try:
    state = ser.readline()
    #print(state)
    return state
  except:
    return ''

def parseMessage(msg):
  # %000060p0&
  print(msg)
  #print(locked)
  
  if (len(msg) == 12 and msg[0] == '%' and msg[7] == 'p'):
    try:
      button = int(msg[8])
    except:
      button = 0
  else:
    button = 0

  return button

def parseWeight(msg):
  # %000060p0&
  if (len(msg) > 9 and msg[0] == '%' and (msg[7] == '&' or msg[9] == '&')):
    try:
      weight = int(msg[1:7])
    except:
      weight = -1
  else:
    weight = -1

  return weight

if __name__ == "__main__":

  states = { 0: standby, 1: turnOn, 2: scale, 3: recipe, 4: timer, 5: startScale, 6: startTimer, 7: startRecipe}
  #  0 : standby
  #  1 : turnOn
  #  2 : scale
  #  3 : recipe
  #  4 : timer
  #  5 : startScale
  #  6 : startTimer
  #  7 : startRecipe

  button = 0
  # 1 : home
  # 2 : scale
  # 3 : timer
  # 4 : recipe
  # 5 : UP
  # 6 : DOWN

  while True:
    message = readSerial()
    button = parseMessage(message)

    print(['B: ', button, 'S: ', state])

    if (locked == True): # locked
      states[0]() # standby
      if (button == 1):
        locked = False
        states[1]() # unlock
        state = 0

    else: # unlocked
      if (state == 0): # from standby ->
        if (button == 2): # -> to startScale
          state = 5
          weight = parseWeight(message)
          states[state](weight)
        elif (button == 3): # -> to startTimer
          state = 6
          states[state]()
        elif (button == 4): # -> to startRecipe
          state = 7
          states[state]()
        else:
          states[state]()

      elif (state == 2): # from scale ->
        if (button == 2): # -> to scale (reset tara)
          weight = parseWeight(message)
          tara = weight
          states[state](weight)
        elif (button == 1): # -> to standby
          state = 0
        elif (button == 3): # -> to startTimer
          state = 6
          states[state]()
        elif (button == 4): # -> to startRecipe
          state = 7
          states[state]()
        else: # -> update weight
          weight = parseWeight(message)
          states[state](weight)

      elif (state == 3): # from recipe ->
        if (button == 6): # -> to recipe (go next step)
          states[state]()
          recipeStep += 1
        if (button == 5): # -> to recipe (go previous step)
          states[state]()
          recipeStep -= 1
        elif (button == 1): # -> to standby
          recipeStep = 0
          state = 0
        elif (button == 3): # -> to startTimer
          recipeStep = 0
          state = 6
          states[state]()
        elif (button == 2): # -> to startScale
          recipeStep = 0
          state = 5
          weight = parseWeight(message)
          states[state](weight)
        else:
          states[state]()

      elif (state == 4): # timer ->
        if (button == 3): # -> resetTimer
          resetTimer()
        elif (button == 1): # -> to standby
          state = 0
          states[state]()
        elif (button == 2): # -> to startScale
          state = 5
          weight = parseWeight(message)
          states[state](weight)
        elif (button == 4): # -> to startRecipe
          state = 7
          states[state]()
        else:
          states[state]()

      elif (state == 5): # startScale -> scale
        state = 2
        weight = parseWeight(message)
        states[state](weight)

      elif (state == 6): # startTimer -> timer
        state = 4
        states[state]()

      elif (state == 7): # startRecipe -> recipe
        state = 3
        states[state]()

    pygame.display.update()

    for event in pygame.event.get():
      if event.type == QUIT:
        ser.close()
        pygame.quit()
        sys.exit()
