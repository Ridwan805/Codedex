import random as rd



print("""1) ✊

2) ✋

3) ✌️

4) 🖖

5) 🦎""")



player = int(input("Enter from 1-3: "))



computer = rd.randint(1,5)

print("You chose: ",player)

print("CPU chose: ",computer)



if player == computer:

  print("Tie")



else:

  if player == 1:#rock

    if computer == 2:#paper

       print("The CPU won")

    elif computer == 3: #scissors

       print("The player won")

    elif computer == 4:#spock

       print("The CPU won")

    elif computer == 5:#lizard

       print("The player won")



  elif player == 2:#paper

    if computer == 1:#rock

       print("The player won")

    elif computer == 3:#scissors

       print("The CPU won")

    elif computer == 4:#spock

       print("The player won")

    elif computer == 5:#lizard

       print("The CPU won")

 

  elif player == 3:#scissors

    if computer == 1:#rock

       print("The CPU won")

    elif computer == 2:#paper

       print("The player won")

    elif computer == 4:#spock

       print("The CPU won")

    elif computer == 5:#lizard

       print("The player won")

 

  elif player == 4:#spock

    if computer == 1:#rock

       print("The player won")

    elif computer == 2:#paper

       print("The CPU won")

    elif computer == 3:#scissors

       print("The player won")

    elif computer == 5:#lizard

       print("The CPU won")



  elif player == 5:#lizard

    if computer == 1:#rock

       print("The CPU won")

    elif computer == 2:#paper

       print("The player won")

    elif computer == 3:#scissors

       print("The CPU won")

    elif computer == 4:#spock

       print("The player won")