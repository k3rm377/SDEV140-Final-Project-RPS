# Program name: Tkinter GUI Game
# Author: Kira Emmett Buck
# Date: 4/22/2022
# Summary: Tkinter window with game and buttons
# Variables:
#   USER_SCORE: the user's kept score
#   COMP_SCORE: the computer's kept score
#   tk: shortened name for pulling tkinter
#   choice_to_number: the choice between rock, paper, or scissors
#   number_to_choice: the number of how many times something was chosen
#   random_computer_choice: random choice of the computer
#   human_choice: another name for user choice

# Import from tkinter
import random 
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Welcome to Rock Paper Scissors") 
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = "" 

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissors':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissors'}
    return rps[number]
def random_computer_choice():
    return random.choice(['rock','paper','scissors']) 

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("It was a tie, try again!")
    elif((user-comp)%3==1):
        print("Nice job! You win!")
        USER_SCORE+=1
    else:
        print("Sorry, the computer won.")
        COMP_SCORE+=1
    text_area = tk.Text(master=window,height=12,width=30,bg="#bad6bc")
    text_area.grid(column=0,row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(tk.END,answer)

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissors'
    COMP_CHOICE=random_computer_choice() 
    result(USER_CHOICE,COMP_CHOICE)

def exitButton (): 
    window.destroy()

button1 = tk.Button(text="       Rock       ",bg="gray",command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text="       Paper      ",bg="white",command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text="      Scissors     ",bg="skyblue",command=scissors)
button3.grid(column=0,row=3)
button4 = tk.Button(text="       Exit       ",bg="red",command=exitButton)
button4.grid(column=0,row=4)


window.mainloop()
