# -*- coding: utf-8 -*-
"""
Developer: André Lascas
Version:1.0.0
"""
import random
from tkinter import *
root = Tk()
entry_string1 = StringVar()
entry_string2 = StringVar()
def get_Keys():
	#Create counters and lists of digits
	random_numbers = []
	random_stars = []
	number_counter = 1
	star_counter = 1
	#Cicle to get 5 numbers and 2 stars without repeated digits
	while number_counter <= 5:
		rand1 = random.randint(1, 50)
		if rand1 not in random_numbers:
			random_numbers.append(rand1)
			number_counter += 1

		if star_counter < 3:
			rand2 = random.randint(1, 11)
			if rand2 not in random_stars:
				random_stars.append(rand2)
				star_counter += 1
	#Sort list in ascending order
	random_numbers.sort()
	random_stars.sort()
	entry_string1.set(','.join(map(str, random_numbers)))
	entry_string2.set(','.join(map(str, random_stars)))
	#Print values
	print ("Numeros: " + str(random_numbers) + "\n" + "Estrelas: " + str(random_stars))


logo = PhotoImage(file="E:\Euromilhoes_Key_Generator\logo_euro.png")
label1 = Label(root, image=logo)
label1.grid(row=0,column=0, columnspan=5)
button1 = Button(root, text='Generate Key!', command=get_Keys)
button1.grid(row=1, column=2)
label2 = Label(root, text='Numbers:')
label2.grid(row=2,column=0)
entry1 = Entry(root, textvariable=entry_string1)
entry_string1.set("")
entry1.grid(row=2,column=1)
label3 = Label(root, text='Stars:')
label3.grid(row=2,column=3)
entry2 = Entry(root, textvariable=entry_string2)
entry_string2.set("")
entry2.grid(row=2,column=4)

root.title('Euromilhões Key Generator')
root.iconbitmap('E:\Euromilhoes_Key_Generator\euromilhoes.ico')
root.mainloop()

