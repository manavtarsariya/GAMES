import random

print("\n")

print("----->",end="")
print("     WELCOME TO THE GAME     ", end="")
print("<-----")
print("")
print("*****",end="")
print("     TIC TAC TOE     ",end="")
print("*****")
print('''
      

     1  | 2  | 3    
    ----|----|-----
     4  | 5  | 6   
    ----|----|-----
     7  | 8  | 9   

      ''')


l = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


dict = { 1 : "O", 2: "X"}
s= set()

def getresult():

    if( l[0][0] == 2 and  l[0][1]==2 and l[0][2] == 2):
        return True
    
    elif(l[0][0] == 1 and  l[0][1]==1 and l[0][2] ==1):
        return False
    
    elif(l[1][0]==2 and  l[1][1]==2 and l[1][2] ==2):
        return True
    
    elif(l[1][0]==1 and  l[1][1]==1 and l[1][2] ==1):
        return False
    
    elif(l[2][0]==2 and  l[2][1]==2 and l[2][2] ==2):
        return True
    
    elif(l[2][0]==1 and  l[2][1]==1 and l[2][2] ==1):
        return False
    
    #colum
    elif(l[0][0]==2 and  l[1][0]==2 and l[2][0] ==2):
        return True
    
    elif(l[0][0]==1 and  l[1][0]==1 and l[2][0] ==1):
        return False
    
    elif(l[0][1]==2 and  l[1][1]==2 and l[2][1] ==2):
        return True
    
    elif(l[0][1]==1 and  l[1][1]==1 and l[2][1] ==1):
        return False
    
    elif(l[0][2]==2 and  l[1][2]==2 and l[2][2] ==2):
        return True
    
    elif(l[0][2]==1 and  l[1][2]==1 and l[2][2] ==1):
        return False
    
    #cross
    elif(l[0][2]==2 and  l[1][1]==2 and l[2][0] ==2):
        return True
    
    elif(l[0][2]==1 and  l[1][1]==1 and l[2][0] ==1):
        return False
    
    elif(l[0][0]==2 and  l[1][1]==2 and l[2][2] ==2):
        return True
    
    elif(l[0][0]==1 and  l[1][1]==1 and l[2][2] ==1):
        return False
    

def you():
    
    a = int(input("please enter a unique number from 1 to 9:")) 
    if (a in s):
        return "\nYou entered wrong choice.\nit is already ocuupied 😠"
    s.add(a)
    if( a == 1):
        l[0][0] = 2

    elif( a == 2 ):
        l[0][1]=2

    elif( a == 3 ):
        l[0][2] = 2

    elif( a == 4 ):
        l[1][0]=2

    elif( a == 5 ):
        l[1][1]=2

    elif( a == 6 ):
        l[1][2]=2
  
    elif( a == 7 ):
        l[2][0]=2
  
    elif( a == 8 ):
        l[2][1]=2
  
    elif( a == 9 ):
        l[2][2]=2
  

    if(getresult() == True):
        print("")
        return "BOOOOM!! \nYOU ARE WINNER 😁"


def comp():
    x = len(s)
    y = x+1

    while(len(s) !=  y):
        computer = random.randint(1,9)
        s.add(computer)

    print(f"computer choose : {computer}")
    if( computer == 1):
        l[0][0] = 1

    elif( computer == 2 ):
        l[0][1] = 1

    elif( computer == 3 ):
        l[0][2] = 1

    elif( computer == 4 ):
        l[1][0] = 1

    elif( computer == 5 ):
        l[1][1] = 1

    elif( computer == 6 ):
        l[1][2] = 1

    elif( computer == 7 ):
        l[2][0] = 1

    elif( computer == 8 ):
        l[2][1] = 1

    elif( computer == 9 ):
        l[2][2] = 1


    if(getresult() == False):
        print("")
        return "UFFFFF!! \nYOU LOOSE THE GAME 😒"

# this method is print result after every iteration
def result():
    print("")
    p=0
    x=0
    m=0
    for i in range(0,3):
        for j in range(0,3):
            m=l[i][j]
            if(m==1):
                print(dict[1] ,end="")
            elif(m==2):
                print(dict[2] ,end="")
            else:
                print(" ",end="")
            
            if(x!=2):
                print(end="    |     ") 
                x=x+1
            elif(x==2):
                x=0

        print("")   
        if(p!=2): 
            print("---- | ----"*2, end="")   
            if(p!=2):
                print(end="---")
        p+=1
        print("")

result()
i=1
while( i != 10):
    if( i % 2 == 0 ):
        y = comp()
        result()
        if(y != None):
            print(y)
            break
    else:
        x= you()
        if(x != None):
            print(x)
            break
    i+=1

else:
    print("")
    print("oppppss! \nmatch is draw 😐")


print("")

p=0
x=0
m=0
for i in range(0,3):
    for j in range(0,3):
        m=l[i][j]
        if(m==1):
            print(dict[1] ,end="")
        elif(m==2):
            print(dict[2] ,end="")
        else:
            print(" ",end="")
        
        if(x!=2):
            print(end="    |     ") 
            x=x+1
        elif(x==2):
            x=0

    print("")   
    if(p!=2): 
        print("---- | ----"*2, end="")   
        if(p!=2):
            print(end="---")
    p+=1
    print("")