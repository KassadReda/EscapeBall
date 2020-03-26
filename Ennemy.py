#coding: utf-8

import sys
import os 
from random import * 
def create(x,y,speed):
	ennemy = dict()
	ennemy['x']= x
	ennemy['y'] = y
	ennemy['speed'] = speed 
	return ennemy
	
def getX(e):
	return e['x']
	
def getY(e):
	return e['y']
	
def getS(e):
	return e['speed']

def setX(e,x) : 
	e['x'] = x
	
def setY(e,y):
	e['y'] = y 
	
def setSpeed(e,speed) : 
	e['speed'] = speed
	
def move(e,dt) : 
	global ennemy
	if e['x'] > 50 :  #modif
		e['x'] = e['x'] - (dt*e['speed'])*10
	else : 
		e['x'] = e['x'] - (dt*e['speed']) 
	if e['x'] < 1 : 
		e['x'] += 100
		e['y'] =  choice(range(2,8))
		
def show(e) :
	
	#on se place a la position de l animat dans le terminal
	
	x=str(int(e["x"]))
	y=str(int(e["y"]))
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)

	#affichage de l animat
	sys.stdout.write("\033[0;91m"+"+\n"+"\033[0m")



