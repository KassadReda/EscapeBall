#coding: utf-8
import sys
import os
import time
timeStep = 1
def create(filename):
	#creation du fond
	bg=dict()
	#ouverture fichier
	myfile = open(filename, "r") 
	chaine = myfile.read() 
	#separation des lignes
	listeLignes=chaine.splitlines()
	
	bg["map"]=[]
	
	#transformation en liste de liste
	for line in listeLignes:
		listeChar=list(line) * 250  # je multiplie mon fichier 250 fois
		bg["map"].append(listeChar) 
	
	myfile.close()
	return bg
	
	
def getChar(bg,x,y,):
	return (bg["map"][y-1][x-1])
	
	
def setChar(bg,x,y,c):
	bg["map"][y-1][x-1]=c
	
	
def getI(bg,x,y,pos): #position skrollée 
	return bg["map"][y][x+int(pos)]	
	
	
def show(bg,pos) : 
	
	global timeStep
	#couleur fond
	sys.stdout.write("\033[22m")
	#couleur whit
	sys.stdout.write("\033[28m")
	map = ""
	#goto	
	for y in range(0,len(bg["map"])):
		for x in range(0,150):   #la taille du fullscreen
			s="\033["+str(y+1)+";"+str(x+1)+"H"
			sys.stdout.write(s)
			sys.stdout.write(bg["map"][y][x+int(pos)])
			
	
			
			
