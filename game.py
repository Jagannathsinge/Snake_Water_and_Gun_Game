import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True  
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Comp turn: Snek(s) Water(w) or Gun(g)?")
randomNum = random.randint(1,3)
print(randomNum)

if randomNum == 1:
    comp = 'S'
elif randomNum == 2:
    comp = 'w'
elif randomNum == 3:
    comp = 'g'

you = input("your turn : Snek(s) Water(w) or Gun(g)?")
a =  gamewin(comp,you)

print(f"computer choose{comp}")
print(f"yours choose{you}")
if a == None :
    print("the game is tie!")
elif a :
    print("you win!")
else:
    print("you lose")