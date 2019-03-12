#importing Libraries
import random

#setting up the variables for the game
nouns = []
verbs = []
adjectives = []

#starting the game
def start():
    print("Welcome to MadLibs 2.0. This will be funny once u enter your information!!")
    nouninput()

#Gets multiple nouns from the user
def nouninput():
    for i in range(4):
        usernoun = input("Enter a noun here: ")
        nouns.append(usernoun)
    verbinput()

#gets multiple verbs from the user
def verbinput():
    for i in range(4):
        userverb = input("Enter a verb here: ")
        verbs.append(userverb)
    adjectiveinput()

#gets multiple adjectives from the user
def adjectiveinput():
    for i in range(4):
        useradjective = input("Enter an adjective here: ")
        adjectives.append(useradjective)
    randompick()




#picks random words to put in the story
def randompick():
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    adjective = random.choice(adjectives)
    verb = random.choice(verbs)
    story(noun1, noun2, adjective, verb)
#puts the random words into the story
def story(noun1, noun2, adjective, verb):
    print("You are a " + adjective + " " + noun1 + " that will die in the year 3081 by " + verb + " into a " + noun2 + ". haha noob you will die :)")
    restart()

#Asks the user if they want the same words, new words, or quit
def restart():
    startover = input("Would you like to use the same words, new words, or quit? Type same/new/quit")
    if startover == "same":
        randompick()
    elif startover == "new":
        nouns.clear()
        verbs.clear()
        adjectives.clear()
        start()
    elif startover == "quit":
        print("wow ok, I guess ur to cool for this")
    else:
        print("please only type same/new or quit")
        restart()
start()
