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
    
    a = int(input("please enter a value, player 1 : ")) 
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
        return "BOOOOM!! \nPLAYER 1 IS WINNER 😁"


def comp():
    b = int(input("please enter a value, player 2 :"))
    if (b in s):
        return "\nYou entered wrong choice.\nit is already ocuupied 😠"
    s.add(b)
    if( b == 1):
        l[0][0] = 1

    elif( b == 2 ):
        l[0][1] = 1

    elif( b == 3 ):
        l[0][2] = 1

    elif( b == 4 ):
        l[1][0] = 1

    elif( b == 5 ):
        l[1][1] = 1

    elif( b == 6 ):
        l[1][2] = 1

    elif( b == 7 ):
        l[2][0] = 1

    elif( b == 8 ):
        l[2][1] = 1

    elif( b == 9 ):
        l[2][2] = 1


    if(getresult() == False):
        print("")
        return "BOOOOM!! \nPLAYER 2 IS WINNER 😁"

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

print(end="")
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
        result()
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