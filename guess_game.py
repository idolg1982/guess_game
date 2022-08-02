from random import *
from statistics import *
from tkinter import N


random = randint(1,100)
counter = 0
print(random)
num = None
lst = []
user = None
best = None

def guess(num1, random1):
  if num1 > random1:
      print("Guess Lower")
  elif num1 < random1:
      print("Guess Higher")
  else:
      print("Correct")
      
def show_score(lst1, counter1):
    print(f"The number of attempts needed to guess correctly: {counter1}")
    print(f"The mean if your guesses: {mean(lst1)}")
    print(f"The median of your guesses: {median(lst1)}")
    print(f"The mode of your guesses: {multimode(lst1)}")



print(""" 
      
        *********************************************************
        *                                                       *
        *                                                       *
        *           Welcome to the Guessing Game!!!             *
        *                                                       *    
        *                                                       *
        *********************************************************  
      
      
      
      """)         
print("Currently no best score, try to set one yourself!")
while user != "no" or user != "n":
    while num!=random:
        try:
            num = input("Enter a guess between 1 - 100: ")
            num = int(num) 
            if num < 1 or num > 100:
                num = input("Try again, the guess needs to be between 1 - 100: ")
                num = int(num)              
        except ValueError:
            print("Oh Oh, we got a guessing error")
        else:
            lst.append(num)
            counter = counter + 1
            guess(num, random)
    show_score(lst, counter)    
    user = input("Would you like to play again? Yes or No: ")
    user = user.lower
    if best == None:
        best = counter   
    if counter < best:
        best = counter
    print(f"The best score to beat is {best}")
    random = randint(1,100)
    counter = 0
    print(random)
    num = None
    lst = None


print("I hope you had fun playing this game!!!")

