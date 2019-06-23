#STONE PAPER SCISSORS

from tkinter import*
from tkinter.messagebox import*
from random import *
Options=["STONE","PAPER","SCISSORS"]
top=Tk()
explanation="""
S
T
O
N
E

P
A
P
E
R

S
C
I
S
S
O
R
S
"""
w2=Label(top,text=explanation,anchor=W,bg="red",fg="white",font=("Times New Roman",25),height=50,width=50)
w2.pack(side=LEFT)
def click1():
	global button_flag
	if button_flag:
		R1.config(bg="blue")
		button_flag = False
	else:
		R1.config(bg="grey")
		button_flag = True
def click2():
	global button_flag
	if button_flag:
		R2.config(bg="blue")
		button_flag = False
	else:
		R2.config(bg="grey")
		button_flag = True
def click3():
	global button_flag
	if button_flag:
		R3.config(bg="blue")
		button_flag = False
	else:
		R3.config(bg="grey")
		button_flag = True
def sel1():
	click1()
	global count
	global win
	global loss
	global tie
	count=count+1
	player="STONE"
	computer=Options[randint(0,2)]
	if player==computer:
		head="TIE!!!!"
		body=head+ "On Round "+str(count)
		tie=tie+1
	elif computer=="PAPER":
		head="OOPS!YOU LOSE!"
		body="Oops!!You lose Round "+str(count)+" !Paper covers Stone"
		loss=loss+1
	else:
		head="CONGRATULATIONS!!!"
		body="Congratulations!!You win Round "+str(count)+" ! Stone smashes Scissors"
		win=win+1
	selection="\t\tRound no:"+str(count)+"/5\n"
	selection+="\t\tUser score:"+str(win)+"/5\n"
	selection+="\t\tComputer score:"+str(loss)+"/5\n"
	selection+="\t\tTie occured:"+str(tie)+"/5\n\n\n"
	body=selection+"User choice:"+player+"\nComputer choice:"+computer+"\n\n"+body
	showinfo(head,body)
	click1()
	if count==5:
		b="\t\tUser score:"+str(win)+"\n\t\tComputer score:"+str(loss)+"\n\n"
		if win>loss:
				h="Congratulations!User is the winner"
		elif loss>win:
				h="Sorry!Computer is the winner!"
		else:
				h="Haha!We have a tie!"
		b=b+"\n\n"+h+"\n\nThanks buddy!\nHad a good time with u!\nHave a nice day!"
		showinfo(h,b)
		count=0
		win=0
		loss=0
		tie=0
def sel2():
	click2()
	global count
	global win
	global loss
	global tie
	global count
	count=count+1
	player="PAPER"
	computer=Options[randint(0,2)]
	if player==computer:
		head="TIE!!!!"
		body=head+ "On Round "+str(count)
		tie=tie+1
	elif computer=="SCISSORS":
		head="OOPS!YOU LOSE!"
		body="Oops!!You lose Round "+str(count)+" !Scissors cuts Paper"
		loss=loss+1
	else:
		head="CONGRATULATIONS!!!"
		body="Congratulations!!You win Round "+str(count)+"! Paper covers stone"
		win=win+1
	selection="\t\tRound no:"+str(count)+"/5\n"
	selection+="\t\tUser score:"+str(win)+"/5\n"
	selection+="\t\tComputer score:"+str(loss)+"/5\n"
	selection+="\t\tTie occured:"+str(tie)+"/5\n\n\n"
	body=selection+"Your choice:"+player+"\nMy choice:"+computer+"\n\n"+body
	showinfo(head,body) 
	click2()
	if count==5:
			b="\t\tUser score:"+str(win)+"\n\t\tComputer score:"+str(loss)+"\n\n"
			if win>loss:
					h="Congratulations!You are the winner"
			elif loss>win:
					h="Sorry!I am the winner!"
			else:
					h="Haha!We have a tie!"
			b=b+"\n\n"+h+"\n\nThnks buddy!\nHad a good time with u!\nHave a nice day!"
			showinfo(h,b)
			count=0
			win=0
			loss=0
			tie=0
def sel3():
	click3()
	global count
	global count
	global win
	global loss
	global tie
	count=count+1
	player="SCISSORS"
	computer=Options[randint(0,2)]
	if player==computer:
		head="TIE!!!!"
		body=head+ "On Round "+str(count)
		tie=tie+1
	elif computer=="STONE":
		head="OOPS!YOU LOSE!"
		body="Oops!!You lose Round "+str(count)+" !Stone smashes Scissors"
		loss=loss+1
	else:
		head="CONGRATULATIONS!!!"
		body="Congratulations!!You win Round "+str(count)+" Scissors cuts paper"
		win=win+1
	selection="\t\tRound no:"+str(count)+"/5\n"
	selection+="\t\tUser score:"+str(win)+"/5\n"
	selection+="\t\tComputer score:"+str(loss)+"/5\n"
	selection+="\t\tTie occured:"+str(tie)+"/5\n\n\n"
	body=selection+"Your choice:"+player+"\nMy choice:"+computer+"\n\n"+body
	showinfo(head,body)
	click3()
	if count==5:
		b="\t\tUser score:"+str(win)+"\n\t\tComputer score:"+str(loss)+"\n\n"
		if win>loss:
				h="Congratulations!You are the winner"
		elif loss>win:
				h="Sorry!I am the winner!"
		else:
				h="Haha!We have a tie!"
		b=b+"\n\n"+h+"\n\nThnks buddy!\nHad a good time with u!\nHave a nice day!"
		showinfo(h,b)
		count=0
		win=0
		loss=0
		tie=0
def sel4():
	manda="RULES"
	akam="""
RULES are simple....
Choose either stone paper or scissors...and try your luck...
1. Stone smashes scissors.Stone wins.
2. Scissors cuts paper.Scissors wins.
3. Paper covers stone.Paper wins.
4. Paper and paper...stone and stone...scissors and scissors...  make a tie

We both have 5 chances.
Each time you win, your score adds up by one...
Each time I win, my score adds up by one...
Tie does not increment or decrement our scores...

Now try ur luck...


			 """
	showinfo(manda,akam)
global count
global win
global loss
global tie
count=0
win=0
loss=0
tie=0
button_flag = True
R4=Button(top,text="RULES",font=("Times New Roman",25),command=sel4)
R4.pack(side=RIGHT, pady=2)
R1=Button(top,text="STONE",font=("Times New Roman",25),command=sel1)
R1.config(bg="grey")
R1.pack(side=LEFT, padx=10, pady=5)
R2=Button(top,text="PAPER",font=("Times New Roman",25),command=sel2)
R2.config(bg="grey")
R2.pack(side=LEFT, padx=5, pady=8)
R3=Button(top,text="SCISSORS",font=("Times New Roman",25),command=sel3)
R3.config(bg="grey")
R3.pack(side=LEFT, padx=5, pady=11)
top.mainloop()