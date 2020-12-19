from tkinter import *
import random
rockpaperscissors=['scissors','rock','paper']
window = Tk()
window.title('Game')
window.geometry('500x700')
score = 'Score: '
play=Label(text="Rock, Paper, Scissors! Press run below to play!", width = 50, height =5, bg='white')
message=Label(text="Computer Choice:", width = 50, height =5, bg='yellow')
score=Label(text='Score: ', width = 50, height =5, bg='lightgreen')
yourchoice=Label(text='Your choice: ', width = 50, height =5, bg='lightblue')
def my_function():
  yourchoice1 = input('Enter rock, paper, or scissors, in lowercase.')
  yourchoice.config(text='Your choice: '+yourchoice1)
  computerchoice = random.choice(rockpaperscissors)
  message.config(text='Computer choice: '+computerchoice) #change message label
  if yourchoice1==computerchoice:
    play.config(text='Tie for this round.')
  elif yourchoice1 == "rock":
    if computerchoice == "paper":
      play.config(text="You lose!")
    else:
      play.config(text="You win!")
  elif yourchoice1 == "paper":
    if computerchoice == "scissors":
      play.config(text="You lose!")
    else:
      play.config(text="You win!")
  elif yourchoice1 == "scissors":
    if computerchoice == "rock":
      play.config(text="You lose...")
    else:
      play.config(text="You win!")
  else:
    play.config(text="That's not a valid play. Check your spelling!")
button = Button(text='Click Me', command = my_function)
play.pack()
message.pack()
yourchoice.pack()
score.pack()
button.pack()

window.mainloop()