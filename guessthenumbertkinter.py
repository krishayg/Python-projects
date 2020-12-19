from tkinter import *
import random
import time
window = Tk()
window.title('Game')
window.geometry("700x500")
label = Label(text="Enter a number.", bg='lightgreen',width = 75, height =5)
label.config(font=("Arial",20))

label.pack()
entry = Entry(width=50)
entry.pack()
loading=Label(text='Guesses: 0', bg='lightblue',width = 75, height =5)
loading.config(font=("Arial",20))

rightnum = random.randrange(1,101)
guesses=0
def check():
  global rightnum 
  global entry
  global guesses
  guesses+=1
  
  try:
    guess=float(entry.get()) #try to convert
  except:
    label.config(text="Invalid Number.")
    return
  loading.config(text='Guesses: '+ str(guesses))
  if guess == rightnum:
    label.config(text='You are correct!!!')
  elif guess > rightnum:
    label.config(text='Your guess is too high.')
  elif guess < rightnum:
    label.config(text='Your guess is too low.')
def my_function():
  check()
button = Button(text='Check', command = my_function)
button.pack()
loading.pack()


window.mainloop()
