# choosing random words
import random
import os
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

printed = False
random_names = [
    "formal", "ultimately", "Formation", "unable", "gaze", "uncle", "gender", "gear", "under", "undergo", "Understand",
    "victory", "video", "view", "gene", "general", "illustrate", "wedding", "image", "Yesterday", "Imagination",
    "Highway", "generate", "impact", "Implication", "implement", "wealthy", "village", "Violation", "violate", "viewer",
    "weapon", "yell", "weather", "highlight", "yellow", "Week", "generation", "yes", "Incorporate", "genetic", "wear",
    "holiday", "highly", "yard", "yeah", "year", "holy", "Home"]
sele = random.choice(random_names)
selected = str(sele)

# length of random selected word
select = list()
for i in selected:
    select += i

length = len(selected)
print("You have choosen", length, "letters word")

# printting dash for the random selected word
dash = list()
x = "_"
while True:
    for i in range(length):
        dash.append(x)
    for i in dash:
        print(i, end=" ")
    print("\n")
    break

# giving choice
choice = 6
while 0 < choice:
    nam = input("enter the letter\n")
    os.system(‘cls’)
    if nam in dash:
        print(f"You have already gussed \"{nam}\" guess another\n")
        for i in dash:
            print(i, end=" ")
        print("\n")
        choice -= 1
        print(stages[choice])

    elif nam in select:
        for i in range(length):
            if select[i] == nam:
                dash[i] = nam
        print("Your guess is correct..")
        print(stages[choice])
        for i in dash:
            print(i, end=" ")
        print("\n")


    else:
        choice -= 1
        print("Your guess is wrong! You lost a life\n")
        print(stages[choice])
        for i in dash:
            print(i, end=" ")
        print("\n")
    if dash == select:
        printed = True
        break
if printed is True:
    print("You won the game")
else:
    print("You last the game..!\n", "The word is ", selected, "\n", "Better luck next time")


