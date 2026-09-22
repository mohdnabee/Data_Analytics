import random 

def game_win(user ,computer): 
    if user == computer:
        return
    
    # Snake vs water
    if user == "s" and computer == "w" :
        return True 
    if user == "w" and computer =="S" : 
        False


    # Water vs Gun 
    if user == "w" and computer == "g" :
            return True 
    if user == "g" and computer =="w" : 
            False


    # Gun vs Snake 
    if user == "g" and computer == "s" :
            return True 
    if user == "s" and computer =="g" : 
            False


rand_no= random.randint(1,3)

print("Computer's turn: Snake (s) , Water (w) ,  Gun (g)")
if rand_no == 1 : 
    computer = "s"
elif rand_no == 2:
    computer = 'w'
else: 
    computer = 'g'

user =  input("Your turn: Snake (s) , Water (w) ,  Gun (g):- " ).lower() 

result = game_win(user,computer)  # Returns true if you win,fale for lose ,  None for draw
print (f"\n You chose:{user}: ")
print (f"\n Computer chose:{computer}")

if result is None : 
    print ("Its a draw !.!.!.")
elif(result):
    print("You win !")
else : 
    print("You Lose !")