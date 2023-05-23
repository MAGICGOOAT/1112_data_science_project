# Python program to create a simple GUI
# Simple Quiz using Tkinter
from random import randint
#import everything from tkinter
from tkinter import *
import textwrap as tw

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

import pandas as pd
import re

#class to define the components of the GUI
class Quiz:
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		self.result = False
  		# no of questions
		self.data_size=len(question)
  		# keep a counter of correct answers
		self.correct=0
		self.need_more_line = [False, False, False, False]
		self.y_pos = 70		
		self.list_A = []
		self.list_B = []
		self.list_C = []
		self.list_D = []
		self.label_list = []
		self.q_list = []
		# set question number to 0
		self.q_no=0
		
		# assigns ques to the display_question function to update later.
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for
		# selected option in a question.
		self.opt_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.check_line()
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		



	def reset_variable(self):
		self.y_pos = 70
		self.need_more_line = [False, False, False, False]
		self.list_A = []
		self.list_B = []
		self.list_C = []
		self.list_D = []
		for x in self.label_list:
			x.destroy()
		for x in self.q_list:
			x.destroy()
		self.label_list = []
		self.q_list = []
  
	def Organize_line(self, line, width):
		total_length = 0
		for i in line:
			if re.search(u'[\u4e00-\u9fff]', i):
				total_length += 2
			else:
				total_length += 1
				
		avg = int(total_length/width)+1
		list = [''] * avg
		list_size = [width] * avg
		current_line = 0
		for i in line:

			if re.search(u'[\u4e00-\u9fff]', i):
				list[current_line] += i
				list_size[current_line] -= 2
			else:
				list[current_line] += i
				list_size[current_line] -= 1
				
			if list_size[current_line] <= 0:
				current_line += 1

		return list
		
			
	
	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
  
		if score == 100:
			self.result = True
		if self.result == True:
			print('True')
		else:
			print('False')
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

	# This method is used to check the answer of the
	# current question by calling the check_ans and question no.
	# if the question is correct it increases the count by 1
	# and then increase the question number by 1. If it is last
	# question then it calls display result to show the message box.
	# otherwise shows next question.
	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			gui.destroy()
		else:
			self.reset_variable()
			self.display_question()
			self.opt_selected=IntVar()
			self.check_line()
			self.opts=self.radio_buttons()
			self.display_options()

	# This method shows the two buttons on the screen.
	# The first one is the next_button which moves to next question
	# It has properties like what text it shows the functionality,
	# size, color, and property of text displayed on button. Then it
	# mentions where to place the button on the screen. The second
	# button is the exit button which is used to close the GUI without
	# completing the quiz.
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(gui, text="Next",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_button.place(x=350,y=460)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=700,y=450)
					

	# This method deselect the radio button on the screen
	# Then it is used to display the options available for the current
	# question which we obtain through the question number and Updates
	# each of the options for the current question of the radio button.
 
	def add_line(self, list1, list2):
		i = len(list1)-1
		while i > 0:
			list2.append(list1[i])
			i-=1
		list2.reverse()
	
	def check_line(self):
		A = self.Organize_line(options_A[self.q_no], 80)
		B = self.Organize_line(options_B[self.q_no], 80)
		C = self.Organize_line(options_C[self.q_no], 80)
		D = self.Organize_line(options_D[self.q_no], 80)
		if len(A) > 1:
			self.need_more_line[0] = True
			self.add_line(A, self.list_A)
		if len(B) > 1:
			self.need_more_line[1] = True
			self.add_line(B, self.list_B)
		if len(C) > 1:
			self.need_more_line[2] = True
			self.add_line(C, self.list_C)
		if len(D) > 1:
			self.need_more_line[3] = True
			self.add_line(D, self.list_D)
  
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		# for a, b, c, d in options_A[self.q_no], options_B[self.q_no], options_C[self.q_no], options_D[self.q_no]:
		A = self.Organize_line(options_A[self.q_no], 80)
		B = self.Organize_line(options_B[self.q_no], 80)
		C = self.Organize_line(options_C[self.q_no], 80)
		D = self.Organize_line(options_D[self.q_no], 80)
		self.opts[val]['text']= A[0]
		self.opts[val+1]['text']= B[0]
		self.opts[val+2]['text']= C[0]
		self.opts[val+3]['text']= D[0]
			


	# This method shows the current Question on the screen
	def display_question(self):
  
		# setting the Question properties
		q = self.Organize_line(question[self.q_no], 60)
		if len(q) > 1:
			for temp_text in q:
				q_no = Label(gui, text=temp_text, font=( 'ariel' ,14, 'bold' ))
				#placing the option on the screen
				self.label_list.append(q_no)
				q_no.place(x=60, y=self.y_pos)
				self.y_pos += 25
			#placing the option on the screen
		else:
			q_no = Label(gui, text=q[0], font=( 'ariel' ,14, 'bold' ))
				#placing the option on the screen
			self.label_list.append(q_no)
			q_no.place(x=60, y=self.y_pos)
			self.y_pos += 25
		


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(gui, text="醫師國考題",
		width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
		
		# place of the title
		title.place(x=0, y=2)


	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# position of the first option
		self.y_pos += 25
		temp = 0
		# adding the options to the list
		while len(self.q_list) < 4:
			# setting the radio button properties
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			value = len(self.q_list)+1,font = ("ariel",12))

			# adding the button to the list
			self.q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 60, y = self.y_pos)
   
			if temp < 4:
				if self.need_more_line[temp] == True:
					if temp == 0:
						
						for x in self.list_A:
							option_ex = Label(gui, text = x, font = ("ariel",12))
							self.label_list.append(option_ex)
							self.y_pos += 22
							option_ex.place(x = 80, y = self.y_pos)
					elif temp == 1:
						for x in self.list_B:
							option_ex = Label(gui, text = x, font = ("ariel",12))
							self.label_list.append(option_ex)
							self.y_pos += 22
							option_ex.place(x = 100, y = self.y_pos)
					elif temp == 2:
						for x in self.list_C:
							option_ex = Label(gui, text = x, font = ("ariel",12))
							self.label_list.append(option_ex)
							self.y_pos += 22
							option_ex.place(x = 100, y = self.y_pos)
					elif temp == 3:
						for x in self.list_D:
							option_ex = Label(gui, text = x, font = ("ariel",12))
							self.label_list.append(option_ex)
							self.y_pos += 22
							option_ex.place(x = 100, y = self.y_pos)
			# incrementing the y-axis position by 40
			self.y_pos += 40
			temp += 1
		# return the radio buttons
		return self.q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("800x550")
gui.minsize(800, 550)
gui.maxsize(800, 550)

# set the title of the Window
gui.title("TEST")

# get the data from the excel file
data = pd.read_excel("data.xlsx")

# set the question, options, and answer
r = randint(0, 197)
data = data.loc[r]

question = [(data['question'])]
options_A = [(data['A'])]
options_B = [(data['B'])]
options_C = [(data['C'])]
options_D = [(data['D'])]

answer = [(data[ 'answer'])]

# question = (data['question'])
# options_A = (data['A'])
# options_B = (data['B'])
# options_C = (data['C'])
# options_D = (data['D'])

# answer = (data['answer'])
# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM
