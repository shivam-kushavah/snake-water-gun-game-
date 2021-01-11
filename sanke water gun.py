import random
lst=['s','w','g']
c,u=0,0
n=4
print("*****************WELCOME TO SNACK WATER GAME********************")
while(n):
    b = random.choice(lst)
    choice = input(f"\n you have {n} life-->\n press--> \n's' for snack, \n'w' for water and  \n'g' for gun: ")
    choice=choice.lower()
    if b==choice:
        print("both are same!! try again")
        n=n+1
    elif b=='s' and choice=='w':
        print(f"you lose!! you choose {choice} and computer choose {b}")
        c+=1
    elif b=='s' and choice=='g':
         print(f"you win!! you choose {choice} and computer choose {b}")
         u+=1
    elif b=='w' and choice=='s':
        print(f"you win!! you choose {choice} and computer choose {b}")
        u+=1
    elif b=='w' and choice=='g':
        print(f"you lose!! you choose {choice} and computer choose {b}")
        c+=1
    elif b=='g' and choice=='s':
        print(f"you lose!! you choose {choice} and computer choose {b}")
        c+=1
    elif b=='g' and choice=='w':
        print(f"you win!! you choose {choice} and computer choose {b}")
        u+=1
    else:
        print("invalid input!! please try again....:\n")
        n=n+1
    n=n-1
print("\n*********************GAME OVER************************\n")
if u>c:
    print(f"\ncongrats!! you are winner.!! your point is {u} and computer point is {c}")
elif u<c:
    print(f"\nsorry!! you are loser!! your point is {u} and computer point is {c}")
else:
    print(f"\nBoth are same!!your point is {u} and computer point is {c} ")
print("\n*********************************thank you*************************************")
