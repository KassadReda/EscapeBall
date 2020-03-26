from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title(" Dicto english")
mainframe = ttk.Frame(root, padding="30 30 120 120")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

word = StringVar()
result = StringVar()

word_entry = ttk.Entry(mainframe, width=70, textvariable=word)
word_entry.grid(column=20, row=10, sticky=(W, E))

def recherche(*args):
	value = word.get()
	con = sqlite3.connect("Dictionary.db")
	cur = con.cursor()
	cur.execute('''SELECT definition FROM entries WHERE word=?''', (value,))
	rows = cur.fetchall()
	"""
	for row in rows : 
		c =  ('{0} : {1}, {2}'.format(rows[0], rows[1], rows[2]))
	# je dois traiter la chaine de caractere 
	"""
	result.set(rows)
	
	cur.close()
	pass

		
	
ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Def it !", command=recherche).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, textvariable=result).grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text=" word :").grid(column=5, row=10, sticky=W)
ttk.Label(mainframe, text=" the definition of this word").grid(column=0, row=0, sticky=W)


root.mainloop()
