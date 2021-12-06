1
5
# | |  0
#----- 1
# | |  2
#----- 3 
# | |  4
#---------------------------------------------------------
#Variables



# drawing Board
#---------------------------------------------------------------------------

def drawBoard(currentField):
    rowsLimit = 5
    columnsLimit = 5
    #Loop for creating rows
    for row in range(rowsLimit):  #0,1,2,3,4
                                  #0,.,1,.,2
        
        if row%2 == 0: # 0,2,4
            #we need 0,2,4 to become 0,1,2 so we can add players values in the board for rows
            practicalRow= int(row/2)
            for column in range(columnsLimit):  #0,1,2,3,4
                                              #0,.,1,.,2
                
                if column%2 == 0: # 0,2,4
                   #we need 0,2,4 to become 0,1,2 so we can add players values in the board for rows
                    practicalColumn = int(column/2)
                    if column != columnsLimit-1:
                        print(currentField[practicalColumn][practicalRow], end = "")
                        #Print(" ", end="") # 1,3 iterations of the loop
                    else:
                        print(currentField[practicalColumn][practicalRow]) #5 iteration of the loop
                        
                else:
                    print("|", end="") #2,4
                     # print(" | | ")
                     #       "12345"
        else:
            print("-----")

#Saving players move in the list
#-----------------------------------------------

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = 1
# To Draw the board first
drawBoard(field)

#-----------------------------------------------
# while loop to keep the players in the play till end of game
while(True):
    print("Players turn: ", player)
    #-------------------------------------------------------------
    # While loop=>check players only can enter integer values between 0 to 2
    while True:
        try:
            moveRow = int(input("Please enter the row:\n"))
            if moveRow in range(3):
                break
            else:
                print("Please input only between 0 to 2") 
                continue
        except ValueError:
            print("Please input integer only...")  
            continue
    while True:
        try:
            moveColumn = int(input("Please enter the column:\n"))
            if moveColumn in range(3):
                break
            else:
                print("Please input only between 0 to 2") 
                continue
            break
        except ValueError:
            print("Please input integer only...")  
            continue
   #-------------------------------------------------  
    # Move for players                
    if player == 1:
        #make move for player 1
        if field[moveColumn][moveRow] == " ":
            field[moveColumn][moveRow] = "X"
            player = 2
    else:
        if field[moveColumn][moveRow] == " ":
            field[moveColumn][moveRow] = "O"
            player = 1
    
    drawBoard(field)   
        
    
                
                                     
         
            
        
    
    

