import random

def login():
  print("Welcome to the Guess The Number")
  username = input("Please enter your username")
  password = input("Please enter your password")

  if username == "1" and password == "2":
    print("Correct you have successfully login to the application")
    return True
  else:
    print("You have entered the wrong login details,Authentication failed")
    return False

def start_game():
  if login():
    number = random.randint(0,100000)
    chances = 0
    
    while chances < 10:
      print("The random number has been generated !!")
      guess = int(input("Guess the number: "))
      chances = chances + 1

      if guess == number:
        print("Congratulations you have won the game")
        break
      
      elif guess < number:
        print("You are closer to the number")
      elif guess > number:
        print("You are far from the number")

    if chances > 10:
      print("Sorry you have run out of your chances,Game Over!!")

start_game()

#Created by Prem chand
