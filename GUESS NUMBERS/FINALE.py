import random

a = random.randint(1,1000)

k = 0
print("only integer number are valids")
while( 1 ):
   
    b = int(input("Now enter your guess :"))
    k +=1
    if( a < b ):
        print(f"please enter a lower number than {b}")
    
    elif( a > b ):
        print(f"please enter a higher number than {b}")
    
    elif( a == b):
        print("yes, you guessed it right")
        break

print(f"you take {k} attemp for guessing a correct number ")