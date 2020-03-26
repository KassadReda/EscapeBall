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
import Ball as Balle
import Ennemy

def getScore(b) : 
	Score = int(Balle.getS(b)/4) #le score est la variable de skroll divisé par 4 

def scores(b) :
	#score 
	Score = int(Balle.getS(b)/4) #le score est la variable de skroll divisé par 4 
	if Balle.getS(b) <= 12:
		print "score : ",0
	elif Balle.getS(b) <= 20000 : 
		print "score : ",Score
	#best score
	bs = open("score.txt", "r") 
	Bs = bs.read() 
	bs.close()
	#on écrit ici dans le fichier le meilleur score
	bestScore=int(Bs)
	bst = open("score.txt", "w")
	if bestScore < Score: 
		bestScore=Score
	bst.write(str(bestScore))	
	bst.close()
	print "best score is",bestScore
	myfile = open("GAME.txt", "r") 
	filer = myfile.read() 
	sys.stdout.write(filer)



