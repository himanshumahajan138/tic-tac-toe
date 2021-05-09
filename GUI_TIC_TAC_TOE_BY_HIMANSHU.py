####################################################################################################
'''THIS IS A GUI TIC TAC TOE GAME CREATED BY "HIMANSHU MAHAJAN"
IT CAN BE PLAYED WITH BOTH HUMAN AND COMPUTER AS WELL
ITS COMPUTER LOGIC IS BASED ON RANDOM NUMBERS'''
####################################################################################################
#importing important libraries
from tkinter import *                            # for gui support 
from tkinter import messagebox                   # for messagebox from tkinter library 
from random import randint                       # for generating random no. (here)
import winsound                                  # for producing  only beep sound (here)
import sys                                       # for closing the program after result (here)
li = ["1","2","3","4","5","6","7","8","9"]       # creating list for progammer and to declare result 
t =  0
lc = []                                          # creating empty list for inserting that places indexes which has occured for computer turn
###########################################################################################################################################################
# defining function for pop up on win or loose with parameter of index in li list 
###########################################################################################################################################################
def message (k):
	global w2,li,sign , compsign,playing ,sign2 
	who = None
	if playing == "c":
		if li[k] == compsign:                   # if sign in matches with sign of computer it means its computer who won
			who = "!!! COMPUTER WON !!!"	
		elif li[k] == sign:
			who = "!!! YOU WON !!!"
	elif playing == "h":
		if li[k] == "X" :
			who = "!!! X WON !!!"
		elif li[k] == "O":
			who = "!!! O WON !!!"
	messagebox.showinfo("!!RESULT!!",who)        # poping out a message if someone won 
	sys.exit()                                   # exiting the program just after result is announced
###########################################################################################################################################################
#creating win or lose or tie function
###########################################################################################################################################################
def result():
	global li, t ,playing
	# creating conditions for winning 
	if li[0] == li[1] == li[2]:
		message(0)
	elif li[3] == li[4] == li[5]:
		message(3)
	elif li[6] == li[7] == li[8]:
		message(6)
	elif li[0] == li[4] == li[8]:
		message(0)
	elif li[0] == li[3] == li[6]:
		message(0)
	elif li[1] == li[4] == li[7]:
		message(1)
	elif li[2] == li[5] == li[8]:
		message(2)
	elif li[2] == li[4] == li[6]:
		message(2)
	#creating conditions for tie
	elif playing == "h":
		if t == 9:
			messagebox.showinfo("!!RESULT!!","!!! GAME IS TIE !!!") # popup ,game is tie if playing with human
			sys.exit()                                              # exiting the program just after TIE is announced
	elif playing == "c":
		if t >9:
			messagebox.showinfo("!!RESULT!!","!!! GAME IS TIE !!!") # popup ,game is tie if playing with computer
			sys.exit()                                              # exiting the program just after TIE is announced
#########################################################################################################################################################
#creating function for HUMAN TURN
#########################################################################################################################################################
def human_turn(u):
	global sign,b1,b2,b3,b4,b5,b6,b7,b8,b9,li,t,lc
    #changing values in list li 
	if u == b1 :
		li[0] = sign    # changing value at index 0 of list li with sign
		t+=1            # updating t after a button is clicked 
		lc.append(1)    # appending in the lc list for computer turn
	elif u == b2 :
		li[1] = sign
		t+=1
		lc.append(2)
	elif u == b3 :
		li[2] = sign
		t+=1
		lc.append(3)
	elif u == b4 :
		li[3] = sign
		t+=1
		lc.append(4)
	elif u == b5 :
		li[4] = sign
		t+=1
		lc.append(5)
	elif u == b6 :
		li[5] = sign
		t+=1
		lc.append(6)
	elif u == b7 :
		li[6] = sign
		t+=1
		lc.append(7)
	elif u == b8 :
		li[7] = sign
		t+=1
		lc.append(8)
	elif u == b9 :
		li[8] = sign
		t+=1
		lc.append(9)
	result()             # calling result function for checking the result 
##########################################################################################################################################################
#creating function button for buttons of board 
##########################################################################################################################################################
def button():
	global b1,b2,b3,b4,b5,b6,b7,b8,b9,playing,li,t,lc
	lt = Label(w2,text  = sign ,bg = "black", fg = "red", font = ("arial",30, "bold", "italic")).place(x = 200 , y = 25) # label for sign of first player
##########################################################################################################################################################
#creating function for disabling and changing text of the button after one click and also for changing the sign of players 
##########################################################################################################################################################
	def disabling(a= None):
		global sign ,human,computer,player1,player2,lt,li,t
		winsound.Beep(250,100)
		if playing == "h":                                  # if playing with human 
			q = True
			while q == True:
				if sign == player1 or sign == player2 :
					player1 , player2 = player2 ,player1   # swaping the values b\w  player 1 and player 2 
					sign = player2
				if sign == "X":                            # sign for label 
					tu = "O"
				elif sign == "O":
					tu = "X"
				# label which changes sign after each turn on the top of window 
				lq = Label(w2,text  = tu ,bg = "black", fg = "red", font = ("arial",30, "bold", "italic")).place(x = 200 , y = 25)
				q = False
				a.configure(state = "disabled" ,fg = "darkorange", text = sign ) # disabling the button which is clicked 
				human_turn(a)                             # calling human_turn function next turn and apply changes in lists
		if playing == "c":                                # if playing with computer 
			# creating function for excluding occupied places from list lc 
			def comp():
				global lc
				exclude = lc
				r  = randint (1,9)                       # generating random no. 
				return comp(d) if r == exclude else r    # returnig r if its not in exclude list else recursion takes place 
			for turn in range (9):                       # creating for loop for computer playing 
				if turn == 0  :                          # here turn goes to human 
					a.configure(state = "disabled" ,fg = "darkorange", text = sign ) # disabling the button clicked 
					human_turn(a)                        # calling human_turn for applying changes in lists and check for result 
				elif turn in [1,3,5,7,9]:                # here turn goes to computer 
					ran = randint(1,9)                   # generating random no. for computer to place on board 
					t+=1                                 # updating the value of t by adding 1 
					if ran == 1:
						if b1["state"] == NORMAL:        # if place is not occupied only then go further to place computer's turn
							b1.configure(state = "disabled" ,fg = "darkorange", text = compsign ) # disabling the button computer choosed 
							li[0] = compsign             # changing the value in list li at certain index
							lc.append(1)                 # appending the place occupied in list lc 
							result()                     # checking whether result is announcable or not 
							break                        # breaking after each turn so that human could start again with their turn 
						else:                            # if place is occupied then comming in else column
							ran = comp()                 # generating a new no. with all occupied places removed 
							continue                     # continuing with next statement  
					elif ran == 2:
						if b2["state"] == NORMAL:
							b2.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[1] = compsign
							lc.append(2)
							result()
							break
						else:
							ran = comp()
							continue
			
					elif ran == 3:
						if b3["state"] == NORMAL:
							b3.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[2] = compsign
							lc.append(3)
							result()
							break
						else:
							ran = comp()
							continue
					elif ran == 4:
						if b4["state"] == NORMAL:
							b4.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[3] = compsign
							lc.append(4)
							result()
							break
						else:
							ran = comp()
							continue
					elif ran == 5:
						if b5["state"] == NORMAL:
							b5.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[4] = compsign
							lc.append(5)
							result()
							break
						else:
							ran = comp()
							continue
					elif ran == 6:
						if b6["state"] == NORMAL:
							b6.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[5] = compsign
							lc.append(6)
							result()
							break
						else:
							ran = comp()
							continue
					elif ran == 7:
						if b7["state"] == NORMAL:
							b7.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[6] = compsign
							lc.append(7)
							result()
							break
						else:
							ran = comp()
							continue
					elif ran == 8:
						if b8["state"] == NORMAL:
							b8.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[7] = compsign
							lc.append(8)
							result()
							break
						else:
							ran = comp()
							continue
					elif ran == 9:
						if b9["state"] == NORMAL:
							b9.configure(state = "disabled" ,fg = "darkorange", text = compsign )
							li[8] = compsign
							lc.append(9)
							result()
							break
						else :
							ran = comp()
							continue
# creating buttons for board 
	b1 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 6.2,pady = 2, activebackground = "darkorange",command = lambda:disabling(b1))
	b2 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 6.8,pady = 2, activebackground = "darkorange",command = lambda:disabling(b2))
	b3 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 9,pady = 2, activebackground = "darkorange",command = lambda:disabling(b3))
	b4 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 6.2,pady = .2, activebackground = "darkorange",command = lambda:disabling(b4))
	b5 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 6.8,pady = .2, activebackground = "darkorange",command = lambda:disabling(b5))
	b6 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 9,pady = .2, activebackground = "darkorange",command = lambda:disabling(b6))
	b7 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 6.2,pady = .2, activebackground = "darkorange",command = lambda:disabling(b7))
	b8 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 6.8,pady = .2, activebackground = "darkorange",command = lambda:disabling(b8))
	b9 = Button(w2, bg = "black" , font = ("arial", 22, "bold"), height = 5 , width = 13,padx = 9,pady = .2, activebackground = "darkorange",command = lambda:disabling(b9))
# placing buttons for board
	b1.place(x=10.2, y = 95.5 )
	b2.place(x = 270.2 , y = 95.5)
	b3.place(x = 533.2 , y = 95.5)
	b4.place(x = 10.2 ,y = 299.5)
	b5.place(x = 270.2 , y = 299.5)
	b6.place(x = 533.2 , y = 299.5)
	b7.place(x = 10.2 , y = 500)
	b8.place(x = 270.2, y = 500)
	b9.place(x = 533.2 , y = 500)
################################################################################################################################################################################
#creating user board
################################################################################################################################################################################
def board(e):
	global human ,computer , player1 , player2 , w2 ,sign,compsign,sign2,bx,bo 
	winsound.Beep(250,100)
	human = None                      # for first time assigning None to required variables
	computer = None
	player1 = None 
	player = None
	compsign = None
	sign = None 
	sign2 = None
	#giving signs to players 
	if e == "x":                      # if human choosed x as their sign on playing with computer 
		human = "X"
		computer = "O"
		sign = human
		compsign = computer 
	elif e == "o":                    # if human choosed o as their sign on playing with computer 
		human = "O"
		computer = "X"
		sign = human
		compsign = computer
	elif e == "h":                    # if playing with human
		if bx == "X":                 # player 1 choosed x
			player1 = "X"
			player2 = "O"
			sign = player1
			sign2 = player2
		elif bo == "O":               # player 1 choosed o
			player1 = "O"
			player2 = "X"
			sign = player1
			sign2 = player2
	w1.destroy()                     # destroying w1 window 
	w2= Tk()
	w2.title("!!TIC TAC TOE!!")
	w2.config(bg = "black")
	w2.geometry("800x700")
	w2.resizable(False,False)
	# creating labels for horizontal lines 
	lh = Label(w2,text = "_ "*33,bg = "black", fg = "red", font = ("arial", 22, "bold")).place(x= 5 , y =58)
	lh = Label(w2,text = "_ "*33,bg = "black", fg = "red", font = ("arial", 22, "bold")).place(x= 5 , y =662)
	lh = Label(w2,text = "_ "*33,bg = "black", fg = "red", font = ("arial", 22, "bold")).place(x= 5 , y =262)
	lh = Label(w2,text = "_ "*33,bg = "black", fg = "red", font = ("arial", 22, "bold")).place(x= 5 , y =462)
    # creating lables for vertical lines
	lv = Label(w2,text = "|"*18,bg = "black", fg = "red", font = ("arial", 21, "bold"),wraplength = 1).place(x= 0 , y = 94)
	lv = Label(w2,text = "|"*18,bg = "black", fg = "red", font = ("arial", 21, "bold"),wraplength = 1).place(x= 260, y = 94)
	lv = Label(w2,text = "|"*18,bg = "black", fg = "red", font = ("arial", 21, "bold"),wraplength = 1).place(x= 789, y = 94)
	lv = Label(w2,text = "|"*18,bg = "black", fg = "red", font = ("arial", 21, "bold"),wraplength = 1).place(x= 523, y = 94)
	# creating other important labels
	l = Label(w2,text  = "TURN -----> ",bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 10 , y = 25)
	l2 = Label(w2,text = "|"*2,bg = "black", fg = "red", font = ("arial", 22, "bold"),wraplength = 1).place(x= 260 , y = 10)
	l2 = Label(w2,text = "|"*2,bg = "black", fg = "red", font = ("arial", 22, "bold"),wraplength = 1).place(x= 523 , y = 10)
	if playing == "c": # if playing with computer 
		# creating important labels 
		ln = Label(w2,text  = "COMPUTER",bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 280 , y = 10)
		ls = Label(w2,text  = compsign,bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 360 , y = 45)
		lh = Label(w2,text  = "HUMAN",bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 580 , y = 10)
		lhs = Label(w2,text  = sign,bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 630 , y = 45)
	if playing == "h": # if playing with human 
		# creating important labels 
		ln = Label(w2,text  = "PLAYER 1",bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 310 , y = 10)
		ls = Label(w2,text  = sign,bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 360 , y = 45)
		lh = Label(w2,text  = "PLAYER 2",bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 570 , y = 10)
		lhs = Label(w2,text  = sign2,bg = "black", fg = "red", font = ("arial",25, "bold", "italic")).place(x = 630 , y = 45)
	button() # calling the function button for further playing and clicking of buttons of board 
	w2.mainloop() # calling the main event loop
############################################################################################################################################################################################
# creating function for clicks of starting windows 
############################################################################################################################################################################################
def click (o):
	global w1,w2,win,bo,bx,playing     # making variables global means they are available outside the loop also
	winsound.Beep(250,100)             # creating beep sound on click of a button of last window (win)
	win.destroy()                      # destroying win window 
	w1 = Tk()                          # creating new window (w1) after win is destroyed 
	w1.config(bg = "black")
	w1.title("TIC TAC TOE")
	w1.resizable(False,False)          # so that window don't get resized 
	playing = o                        # changing parameter to a variable 
# creating window for computer
	if playing == "c":                 # condition for playing with computer 
		w1.geometry("600x240")
		# defining important labels 
		l = Label(w1,text = "!!PLAYING WITH COMPUTER!!" ,font = ("airal", 25,"bold", "italic","underline"),fg = "darkorange", bg ="black").place(x=60,y=25)
		l = Label(w1,text = "!!CHOOSE YOUR SIGN!!" ,font = ("airal", 25,"bold", "italic"),fg = "darkorange", bg ="black").place(x=80,y=100)
		# defining important buttons 
		b2 = Button(w1, text = "X",bg = "darkorange", fg = "black",width =3, font = ("arial",20,"bold","italic"), relief = FLAT ,command =  lambda:board("x")).place(x = 180 ,y = 160)
		b3 = Button(w1, text = "O",bg = "darkorange", fg = "black",width =3 , font = ("arial",20,"bold","italic"), relief = FLAT ,command =  lambda:board("o")).place(x = 360, y = 160)		
#creating window for humans
	elif playing =="h":                            # condition for playing with human
		w1.geometry("650x430")
		#creating function for sign of player1 
		def player1(q):
			global bx , bo
			winsound.Beep(250,100)
			if q == "x":
				bx.configure(state = "disabled")   #disabling button after on click
				bo.configure(state = "disabled")   # disabling second button also to insure not clicking 
				if bx["state"] == DISABLED:
					be.place(x = 215, y = 320)     # placing enter button after bx button is clicked 
					bx = "X"                       # assigning sign(x) to player 1 
			elif q == "o":
				bo.configure(state = "disabled")
				bx.configure(state = "disabled")
				if bo["state"] == DISABLED:
					be.place(x = 215, y = 320)
					bo = "O"
		# creating important labels 
		l = Label(w1,text = "!!PLAYING WITH HUMAN!!" ,font = ("airal", 30,"bold", "italic","underline"),fg = "darkorange", bg ="black").place(x=70,y=25)
		l = Label(w1,text = "!!FIRST PLAYER!!" ,font = ("airal", 30,"bold", "italic"),fg = "darkorange", bg ="black").place(x=130,y=100)
		l = Label(w1,text = "!!CHOOSE YOUR SIGN!!" ,font = ("airal", 30,"bold", "italic"),fg = "darkorange", bg ="black").place(x=70,y=160)
		# creating important buttons
		bx = Button(w1, text = "X",bg = "darkorange", fg = "black",width =3, font = ("arial",20,"bold","italic"), relief = FLAT ,command =  lambda:player1("x"))
		bo = Button(w1, text = "O",bg = "darkorange", fg = "black",width =3 , font = ("arial",20,"bold","italic"), relief = FLAT ,command =  lambda:player1("o"))
		be = Button(w1, text = "ENTER",bg = "darkorange", fg = "black",height = 2,width= 10, font = ("arial",20,"bold","italic"), relief = FLAT ,command =  lambda:board("h"))
		bx.place(x = 180 ,y = 230)                 # placing buttons 
		bo.place(x = 360, y = 230)
	w1.mainloop()                                  # to run main event loop
############################################################################################################################################################################################################################
#creating starting window 
############################################################################################################################################################################################################################
win = Tk()                                        #this will create a window named win
win.config(bg = "black")                          # this will give black colour to background of win window
win.title("TIC TAC TOE BY HIMANSHU ")             # for title on win window 
win.geometry("1015x730")                          # for having this size when in mini window 
win.state("zoomed")                               # for having always maximised window
# defining important labels
l = Label (win ,text = "!!WELCOME TO TIC TAC TOE GAME BY HIMANSHU!!",font = ("arial",29,"bold","italic","underline"),fg = "darkorange",bg = "black").place(x = 15 ,y = 50)
l1 = Label (win ,text = "--------->>>>>>>",font = ("arial",30,"bold"),fg = "darkorange",bg = "black").place(x = 10 ,y = 270)
l1 = Label (win ,text = "--------->>>>>>>",font = ("arial",30,"bold"),fg = "darkorange",bg = "black").place(x = 10 ,y = 520)
# defining important buttons 
b1 = Button(win, text = "WANT TO PLAY WITH COMPUTER",bg = "darkorange", fg = "black", font = ("arial",20,"bold","italic"), relief = FLAT , height = 2 , width = 40,command =  lambda:click("c")).place(x = 320, y = 250)
b1 = Button(win, text = "WANT TO PLAY WITH HUMAN",bg = "darkorange", fg = "black", font = ("arial",20,"bold","italic"), relief = FLAT, height = 2 , width = 40,command = lambda:click("h")).place(x = 320, y = 500)
win.mainloop()                                    # to run main event loop
############################################################################################################################################################################################################################