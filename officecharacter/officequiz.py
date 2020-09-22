#!/usr/bin/env python3
from time import sleep

char= ["Michael Scott", "Dwight K. Shrute", "Jim Halpert", "Toby Flenderson"]
paper_list= ["printer paper", "papyrus", "paper bag", "wrapping paper"]
career_list= ["sports agent", "CEO", "farmer", "writer"]
worst_list= ["stupidity", "noise", "rules", "rejection"]

total = 0
print()
print("Which Office Character are you? Michael, Dwight, Jim or Toby?") ; sleep(0.8)
print()
print("Answer the following questions to reveal your Office Character.") ; sleep(0.8)
print()
paper= input("Pick a type of paper: printer paper, papyrus, paper bag, wrapping paper.").lower()

#while paper not in paper_list:
if paper == "printer paper":
    total +=4
elif paper == "papyrus":
    total =+2
elif paper == "paper bag":
    total +=1
elif paper == "wrapping paper":
    total +=3
else:
    print("False, Black Bear is best...choose again!")
print()
career= input("Pick a career: CEO, sports agent, writer, farmer.").lower()

if career == "ceo":
    total +=4
elif career == "sports agent":
    total =+3
elif career == "farmer":
    total +=2
elif career == "writer":
    total +=1
else:
    print("False, Black Bear is best...choose again!")
print()
worst= input("What are you worst at dealing with: rules, stupidity, rejection, noise?").lower()

if worst == "rejection":
    total +=4
elif worst == "rules":
    total =+3
elif worst == "stupidity":
    total +=2
elif worst == "noise":
    total +=1
else:
    print("False, Black Bear is best...choose again!")


print(" ") ; sleep (0.2)
print("Y") ; sleep (0.2)
print("O") ; sleep (0.2)
print("U") ; sleep (0.2)
print(" ") ; sleep (0.2)
print("A") ; sleep (0.2)
print("R") ; sleep (0.2)
print("E") ; sleep (0.2)
print(" ") ; sleep (0.2)
print(" ") ; sleep (0.2)



if total > 9:
    print("Michael Scott! That's what she said! is your favorite line, and you moved to Colorado with Holly to start the Space Force!")
elif total < 10 and total > 6:
    print("Jim Halpert! You enjoy cycling and all the Philly sports teams! You left to start Some Good News!")
elif total < 7 and total > 3:
    print("Dwight K. Shrute! You finally got promoted from Assistant To the Regional Manager to Regional Manager. You can now sell your beet farm.")
elif total < 4:
    print("Toby Flenderson. Your greatest achievement in life is being a juror for the Scranton Strangler. On the side you write mystery novels.")



