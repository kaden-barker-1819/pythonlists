#importing variables
import random
import turtle
import time
import tkinter



#window...
window = turtle.Screen()
window.bgcolor("black")

#puts underlines under each letter
under = turtle.Turtle()
under.color("red")
under.pensize(4)
under.shape("turtle")
under.speed(10)

# the Turtle
jim = turtle.Turtle()
jim.color("red")
jim.pensize(4)
jim.shape("turtle")
jim.speed(20)
jim.hideturtle()
#this is the words list
randomwords = ["bungler", "banjo", "fjord", "polka", "yo", "rogue"]

wrongcount = 0
rightcount = 0

#selects random word from list
def start():
   global word
   global wordlist
   word = random.choice(randomwords)
   print(word)
   wordlist = []
   for char in word:
       wordlist.append(char)
   underscores()


#draws hanging machine
def hangjim():
   jim.left(180)
   jim.forward(200)
   jim.back(100)
   jim.right(90)
   jim.forward(250)
   jim.right(90)
   jim.forward(100)
   jim.right(90)
   jim.forward(25)
   jim.right(90)


#counts wrong letters guessed by the player

def wrongcounter():
   global wrongcount
   if wrongcount == 1:
       jimhead()
   elif wrongcount == 2:
       jimbody()
   elif wrongcount == 3:
       jimleftarm()
   elif wrongcount == 4:
       jimrightarm()
   elif wrongcount == 5:
       jimleftleg()
   elif wrongcount == 6:
       jimrightleg()
   print("hi")
   winloser()



#draws head
def jimhead():
   jim.circle(20)
   jim.circle(20,180)
   jim.right(90)
   guess()

#draws the body
def jimbody():
   jim.forward(100)
   guess()

#draws left arm
def jimleftarm():
   jim.back(75)
   jim.right(45)
   jim.forward(35)
   guess()


#draws right arm
def jimrightarm():
   jim.back(35)
   jim.left(90)
   jim.forward(35)
   guess()
#draws the left leg
def jimleftleg():
   jim.back(35)
   jim.right(45)
   jim.forward(75)
   jim.right(45)
   jim.forward(50)
   guess()
# draws the right leg
def jimrightleg():
   jim.back(50)
   jim.left(90)
   jim.forward(50)

#user inputs letter


# output = ['_'] * len(word)
def guess():
   global wordlist
   global word
   global wrongcount
   global rightcount
   miss = len(word)
   letter = input ("Guess a letter please ")
   for i in range(len(wordlist)):
       print("joke")
       if letter.lower() == wordlist[i]:
           print(rightcount)
           drawletter(i, letter)
       else:
           print("hi")
           miss-= 1
   if miss == 0:
       wrongcount += 1
       print("bye")
       wrongcounter()
   else:
       print(rightcount)
       rightcount += 1
       print(rightcount)
       winloser()
#puts wrong letters to the side





def underscores():
   global word
   global wordlist
   under.hideturtle()
   under.penup()
   under.goto(-250,-250)
   under.pendown()
   wordlength = len(word)
   for i in range(wordlength):
       under.write ("_   ", font = ("arial", 50, "normal"))
       under.pu()
       under.forward(50)
       under.pd()
   guess()

#corrects letter go in correct spot
def drawletter(i, letter):
   under.pu()
   under.goto(-250, -250)
   under.forward(50* i)
   under.pd()
   under.write(letter, font = ("Arial", 50, "bold"))
   guess()

#determins winner/loser
def winloser():
   global wrongcount
   global rightcount
   global word
   print(rightcount)
   if wrongcount == 6:
        jim.write("You Died!!", font = ("arial", 50, "bold"))
        print(wrongcount)
        startover()
   elif rightcount == len(word):
       jim.write("You Win", font = ("arial", 50, "bold"))
       startover()
   else:
       print("guess")
       guess()
#restart

def startover():
   restart = input("Would like to start over?? yes/no ")
   if restart == ("yes"):
       jim.reset()
       under.reset()
       start()
   elif restart == ("no"):
       print("Wow ok, Thanks for playing")

   else:
       print("Please only type yes or no")
       startover()


hangjim()
start()
window.exitonclick()



