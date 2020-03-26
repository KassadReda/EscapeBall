# coding: utf-8
import sqlite3
import sys 
import os

def ask_word():
	print(" le mot :: ? \n")
	word = input(" == ")
	return word
	
def ask_type_word():
	print(" le type du mot  \n" )
	type_word = input("==")
	return type_word

def ask_defi():
	print(" la definition du mot  \n" )
	defi = input("==")
	return defi
	

def recherche(word):
	con = sqlite3.connect("Dictionary.db")
	cur = con.cursor()
	cur.execute('''SELECT * FROM entries WHERE word=?''', (word,))
	rows = cur.fetchall()
	return rows
	cur.close()
#fonction ajouter un mot qui n'existe pas dans la DB 
def add_word(Nom, Region, Note):
	con = sqlite3.connect("Dictionary.db")
	cur = con.cursor()
	cur.execute('''INSERT INTO entries (word,wordtype,definition)
    VALUES (?,?,?)''',(Nom,Region,Note))
    
	row = cur.fetchone()
	con.commit()
	cur.close()
	
#fonction pour supprimer un mot ajouté via la fonction ci haut 

def sup_word(word,defi):
	
	con = sqlite3.connect("Dictionary.db")
	cur = con.cursor()
	cur.execute('''DELETE FROM entries WHERE word=? and definition =?''', (word,defi,))
	row = cur.fetchone()
	con.commit()
	cur.close()

# lister tt les mots de la bdd

def listing():
	con = sqlite3.connect("Dictionary.db")
	cur = con.cursor()
	cur.execute('''SELECT word FROM entries''')
	rows = cur.fetchall()
	return rows





