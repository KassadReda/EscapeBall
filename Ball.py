#coding: utf-8
import sys
import os

def create(x,y,xm,speed) :
    ball = dict()
    ball['x']= x
    ball['y'] = y
    ball['xm'] = xm
    ball['speed'] = speed
    return ball
    
    
def getX(b) : 
	return b['x']
	
def getY(b) : 
	return b['y']
	
def getSpeed(balle) : 
	return balle['speed']
	
def setSpeed(b,speed):
	b['speed'] = speed
	
	
def getS(balle):
	return balle['xm']
	
def setX(b,x) : 
	b['x'] = x 
	
def setY(b,y) : 
	b['y'] = y 
	 
def setS(b,xm) : 
	b['xm'] = xm 
	
	
def move(b,dt) : #skroll
	b['xm'] = b['xm'] + (dt*b['speed'])



def show(b) :
	#on se place a la position de l animat dans le terminal
	x=str(int(b["x"]))
	y=str(int(b["y"]))
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)

	#couleur fond noire
	sys.stdout.write("\033[12m")

	#affichage de l animat
	sys.stdout.write("\033[0;33m"+"O\n"+"\033[0m")
	
def moveUp(b): 
	b["y"] = b["y"] - 1
	
def moveDown(b):
	b["y"] = b["y"] + 1

	
	
