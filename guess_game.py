from random import *
from statistics import *



random = randint(1,100)
counter = 0
#print(random)
num = None
lst = []
user_input = ""
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
while user_input != 'no':
    while num!=random:
        try:
            num = int(input("Enter a guess between 1 - 100: "))
            while num < 0 or num > 101:
                print("Oh Oh, we got a guessing error")
                num = int(input("Enter a guess between 1 - 100: "))                                                           
        except ValueError:
            print("Oh Oh, we got a guessing error")
        else:
            lst.append(num)
            counter = counter + 1
            guess(num, random)
    show_score(lst, counter)
    if best == None:
        best = counter   
    if counter < best:
        best = counter
    print(f"The best score to beat is {best}")        
    user_input = input("Would you like to play again? Yes or No: ")
    user_input = user_input.lower()
    if user_input == 'n':
        user_input = 'no'
    random = randint(1,100)
    counter = 0
    #print(random)
    num = None
    lst.clear()


print("I hope you had fun playing this game!!!")

