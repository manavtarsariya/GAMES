import random

s = set()
f = set()


print("")
print("           WELCOME TO THE GAME            ")
print("")
print("           -----> BINGO <-----            ")

# p = list , f = set
def generate(f,p):
    i=0
    j=0 
    while(len(f) != 25):  
            x= random.randint(1,25)
            z = len(f)
            f.add(x)

            if(len(f) == z+1):
                p[i][j] = x
                j=j+1
                if(j==5):
                    i=i+1
                    j=0

    print("")


# p = list
def step(p):
    i=0
    j=0
 
    print("|--------"*5,end="")
    print("|")
    for i in range(0,5):
        for j in range(0,5):
            if(j==0):   
                print("|   ",end="")

            if( p[i][j] == "👌" or p[i][j] == "🤞" ):
                print(f"{p[i][j]}",end="")
                print(end="   |   ")

            elif( p[i][j] < 10 ):
                print(f"{p[i][j]}",end="")
                print(end="    |   ")
    
            else:
                print(f"{p[i][j]}",end="")
                print(end="   |   ")
        print("")
        print("|--------"*5,end="")
        print("|")

print("")


def check_row(i,list):
    u=0
    res = 0
    for j in range(0,5):
        h = list[i][j]
        if ( h == "👌" or h == "🤞" ):
            u = u+1
    if(u == 5): 
        return 1


def check_colum(j,list):
    u=0
    res=0
    for i in range(0,5):
        h = list[i][j]
        if ( h == "👌" or h == "🤞" ):
            u = u+1
    if(u == 5):
        return 1
    

def check_cross(list):
    u=0
    res=0
    for i in range(0,5):
        h = list[i][i]
        if ( h == "👌" or h == "🤞" ):
            u = u+1
    if(u == 5):
        return 1
    

def check_cross2(list):
    u = 0
    i = 0
    j = 4

    while(i != 5 ):
        h = list[i][j]
        if ( h == "👌" or h == "🤞" ):
            u = u+1
        i = i + 1
        j = j - 1
    if(u == 5):
        return 1
    
    
def getresult(list):
    finale_result = 0

    for i in range(0,5):
        ru = check_row(i,list)
        if( ru == 1):
            finale_result = finale_result + 1
        if ( finale_result == 5):
            return 1

    
    for i in range(0,5):
        x = check_colum(i,list)
        if( x == 1):
            finale_result = 1 + finale_result
        if ( finale_result == 5):
            return 1

    
    y = check_cross(list)
    if( y == 1):
            finale_result = 1 + finale_result
    if ( finale_result == 5):
        return 1
    
    z = check_cross2(list)
    if(z == 1):
            finale_result = 1 + finale_result
    if ( finale_result == 5):
        return 1
    


player_1 = input("enter a name of player 1 :")
player_2 = input("enter a name of player 2 :")


# p1 = set()
# p2 = set()

ps = set()

def moves(l,v,p):
    i=0
    j=0
    q=0
    m = int(input("enter your choice :"))
    for i in range(0,5):
        for j in range(0,5):
            y = l[i][j]

            if( m > 25 or m <= 0):
                print("something went wrong")
                return "something went wrong"
               
            
            elif( m in ps): 
                print(f"{m} is already removed")
                return "given element is already removed"
              
            
            elif(y == m and (v%2!=0)):
                l[i][j] = "🤞"
                ps.add(m)

                for u in range(0,5):
                    for n in range(0,5):
                        q = p[u][n]
                        if(q == m):
                            p[u][n] = "👌"
            
                w = getresult(l)
                if( w == 1):
                    return 2
                return print(f"{m} is removed")
            
            
            elif(y == m and (v%2==0)):
                l[i][j] = "👌"
                ps.add(m)

                for u in range(0,5):
                    for n in range(0,5):
                        q = p[u][n]
                        if(q == m):
                            p[u][n] = "🤞"

                
                xe = getresult(l)
                if( xe == 1):
                    return 2
                return print(f"{m} is removed")

                
l = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0], 
]

p = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0], 
]



print("")
print(f" this box is for {player_1}")
generate(s,l)
step(l)
print("")
print("")
print(f" this box is for {player_2}")
generate(f,p)
step(p)


v = 1 
while( v != 25):
    if( v % 2 == 0):
        print(f"{player_2.upper()} currently deleted values are : {ps}")
        print(f"{player_2.upper()},",end="")
        x = moves(p,v,l)
        
        if ( x == "something went wrong" or x == "given element is already removed" ):
            break

        elif(x == 2):
            step(p)
            print(f"WOOHOOOOOO!!!!! \n{player_2.upper()}, YOU ARE WINNER 🥳🥂")
            print(f"OOOOPPPSSS!!!!! \n{player_1.upper()}, YOU ARE LOOSER 😒😑")
            break
        step(p)
       

    else:
       
        print(f"{player_1.upper()} currently deleted values are : {ps}")
        print(f"{player_1.upper()},",end="")
        x = moves(l,v,p)

        if ( x == "something went wrong" or x == "given element is already removed"):
            break

        elif(x == 2):
            step(l)
            print(f"WOOHOOOOOO!!!!! \n{player_1.upper()}, YOU ARE WINNER 🥳🥂")
            print(f"OOOOPPPSSS!!!!! \n{player_2.upper()}, YOU ARE LOOSER 😒😑")
            break
        step(l)
        

    v=v+1

