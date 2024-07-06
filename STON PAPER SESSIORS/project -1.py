'''

1 for rock 
2 for paper
3 for sessiors

'''

import random

n = [1, 2, 3]
r = random.choice(n)
# print(r)

me = input("enter your choice : ")
dict = {"r":1 , "p":2, "s":3}
me_num = dict[me]
# print(me_num)

revdict = {1: "rock" , 2: "paper", 3:"sessiors"}

print(f"you choose : {revdict[me_num]} \ncomputer choose : {revdict[r]}")


if( r == me_num):
    print("it's a draw! 😐 ")

else:
    if((r==1) and me_num==2):
        print(" YOU WIN! 😁")

    elif(r==1 and me_num==3):
        print(" YOU MESED UP!😒")
    
    elif(r==2 and me_num==1):
        print(" YOU MESED UP!😒")

    elif(r==2 and me_num==3):
         print(" YOU WIN! 😁")

    elif(r==3 and me_num==1):
        print(" YOU WIN! 😁")

    elif(r==3 and me_num==2):
        print(" YOU MESED UP!😒")