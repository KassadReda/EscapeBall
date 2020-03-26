#coding: utf-8

import sys
import os
import time
import termios
import tty
import select
from random import randint,choice
#mesModules
import Background
import Ball
import Ennemy
import Score
old_settings = termios.tcgetattr(sys.stdin)
#donnee du jeu
ball=None
background = None
ennemy = None
ennemy2 = None
ennemy3 = None
mapy = raw_input("choississez une map 1 pour la classic flappy bird ou 2 pour la spéciale escape ball :")
back = ["a.txt","image.txt"] #liste de maps
fichier = choice(back)  #choix aléatoire par defaut


def init() :
    global  ball, background, ennemy, ennemy2, ennemy3, mapy
    timeStep= 0.1
    ball = Ball.create(x = 2.0,
                         y = 5.0,
                         xm = 1.0,
                         speed = 4) 
    
    ennemy = Ennemy.create(x = 140,
						   y = randint(2,8),  
						   speed = 5)
    ennemy2 = Ennemy.create(x = 170,
							y = randint(2,8),
							speed = 5)
    ennemy3 = Ennemy.create(x = 300,
							y = randint(2,8),
							speed = 5)
	#choix de map
    if mapy == '2' :
    	background = Background.create(back[0])
    elif mapy == '1':
    	background = Background.create(back[1])
    else :
		background = Background.create(fichier)  
    tty.setcbreak(sys.stdin.fileno())
    
    
def interact() : 
	global ball, background, timeStep
	if isData():
		c = sys.stdin.read(1)
		if c == '\x1b':         # x1b is ESC
			quitGame()
		elif c=='a' :
			Ball.moveUp(ball)
		elif c=='x' : 
			Ball.moveDown(ball)

#collision entre la map et la balle
def checkColide():
	global ball, background, ennemy
	y= (Ball.getY(ball)) - 1  #-1 les deux y,x
	x = ball['x'] - 1
	if Background.getI(background,int(x),int(y),Ball.getS(ball)) == '-'  : 
		sys.stdout.write("crashed on the borders"+"\n")
		quitGame()
		
#collision entre la balle et les ennemies	
def colide():
	global ennemy, ball, ennemy2, ennemy3
	if ennemy['x'] == ball['x'] and ennemy['y'] == ball['y'] : 
		print " killed by the computer "
		quitGame()
	elif ennemy2['x'] == ball['x'] and ennemy2['y'] == ball['y'] :
		print " killed by the computer "
		quitGame()
	elif ennemy3['x'] == ball['x'] and ennemy3['y'] == ball['y'] : 
		print " killed by computer "
		quitGame()
		
			
def isData() : 
	 return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
	 
#supprimer la derniere commande du clavier	 
def flush():
	termios.tcflush(sys.stdin, termios.TCIOFLUSH) 
	
	
def live(dt): 
	global ball, ennemy, ennemy2, ennemy3
	Ball.move(ball,dt)
	Ennemy.move(ennemy,dt)
	Ennemy.move(ennemy2,dt)
	Ennemy.move(ennemy3,dt)
	
	
def show():
    global ball, background, ennemy, ennemy2, ennemy3
    
    sys.stdout.write("\033[1;1H")
    sys.stdout.write("\033[2J")
	#affichage des different element
    Background.show(background,Ball.getS(ball))
    Ball.show(ball)
    Ennemy.show(ennemy)
    Ennemy.show(ennemy2)
    Ennemy.show(ennemy3)
    #restoration couleur
    sys.stdout.write("\033[26m")
    sys.stdout.write("\033[22m")
    #deplacement curseur
    sys.stdout.write("\033[0;0H\n")
    
    
def run() :
	global ball, background
	while 1:
		interact()
		checkColide()
		colide()
		flush()
		os.system("clear")
		show()
		live(0.2)  #0.2
		#le jeu devient de plus en plus rapide en avançant dans le jeu 
		timeStep = 0.1
		if Score.getScore >= 10 : 
			timeStep -= 0.04
		elif Score.getScore >= 50 : 
			timeStep -= 0.03
		elif Score.getScore >= 100 :
			timeStep -= 0.02
			
		time.sleep(timeStep)  
	os.system("clear")
	
	
def quitGame():	
	global background, ball
	#restoration parametres terminal
	global old_settings
	os.system("clear")
	
	#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	
	Score.scores(ball)
	#pour jouer une seconde partie
	askContinueGame()
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
	sys.exit()

def askContinueGame() : 
	button = raw_input()
	if button == '\x1b' : 
		sys.exit()
	else : 
		game()
		
def game() : 
	init()
	run()


game()

