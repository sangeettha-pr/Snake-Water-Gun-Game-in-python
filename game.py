import random 

print("Comp turnn: Snake(1),Water(2),Gun(3)?")
ran_num=random.randint(1,3)
if ran_num==1:
    comp='s'
if ran_num==2:
    comp='w'
if ran_num==3:
    comp='g'

# print(ran_num)
b=input("Your turn:Snake(s),Water(w),Gun(g)?")
if comp=='s' and b=='s'or comp=='w' and b=='w'or comp=='g' and b=='g':
    print("Draw!!,Try again")
elif comp=='s' and b=='w':
   print("Computer Won!")
elif comp=='s' and b=='g':
    print("You Won!")
elif comp=='w' and b=='s':
    print("You Won!")
elif comp=='w' and b=='g':
   print("Computer Won!")
elif comp=='g' and b=='s':
   print("Computer Won!")
elif comp=='g' and b=='w':
    print("You Won!")
else:
    print("Wrong choice ! try again")
print("Computer's choice:",comp)
print("Your choice:",b)
