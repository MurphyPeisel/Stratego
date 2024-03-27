import arcade

START_X = -1
START_Y = -1

FLAG_POWER = 0
BOMB_POWER = 12
MARSHALL_POWER = 10
GENERAL_POWER = 9
COLONEL_POWER = 8
MAJOR_POWER = 7
CAPTAIN_POWER = 6
LIEUTENANT_POWER = 5
SERGEANT_POWER = 4
MINER_POWER = 3
SCOUT_POWER = 2
SPY_POWER = 1

class Piece():
    type = None   #Piece types, Lake, Nothing, etc.
    power = None
    posX = None
    posY = None
    Hidden = None
    
    def __init__ (self, type, power, x, y):        
        self.type = type
        self.power = power
        self.posX = x
        self.posY = y
    
    def getType(self):
        return self.type
    def getPower(self):
        return self.power
    def getPosition(self):
        pos = [self.posX, self.posY]
        return pos
    
    def setPosition(self, x, y):
        self.posX = x
        self.posY = y

    def draw(self):
        arcade.draw_text(f"{self.power}",
                         self.posX,
                         self.posY,
                         arcade.color.RED,
                         20, bold=True,
                         font_name = "Kenney Future")
        

column = [Piece] * 10

#During Gameplay
def movePiece(piece, x,y):
    #CHECK IF LAKE
    if(column[y][x] == "[ ]"):
        return "LAKE"
    piece.setPosition(x, y)
    #CHECK IF POSITION IS OCCUPIED
    if(column[y][x] == "P"):
        #reveal enemy peice
        "hooray"
        #compare peice powers
        
        #capture the peice with the lower power


#SETUP
def placePiece(P1):
    
    x = P1.getPosition()[0]
    y = P1.getPosition()[1]
    if(column[y][x] == "[ ]"):
        return "Position not Available: LAKE"
    elif(column[y][x] != "---"):
        return "Position not Available: Taken"
    else:
        column[y][x] = P1.getType()
        return f"{P1.getType()} Placed Succesfully"


#Creates a 10x10 Grid
def createGrid():
    for i in range(10):
        row = [Piece] * 10
        for j in range(10):
            row[j] = "---"
        column[i] = row

        
    column[4][2] = "[ ]"
    column[4][3] = "[ ]"
    column[5][2] = "[ ]"
    column[5][3] = "[ ]"
 

    column[4][6] = "[ ]"
    column[4][7] = "[ ]"
    column[5][6] = "[ ]"
    column[5][7] = "[ ]"


def printGrid():    
    for i in range(10):
        print(column[i])
        

#Initialize 40 pieces per player
def initPieces():
    p1 = []
    #FLAG
    Flag = Piece("Flg", FLAG_POWER, START_X, START_Y)
    p1.append(Flag)
    
    #BOMBS
    Bomb1 = Piece("Bom", BOMB_POWER, START_X, START_Y)
    Bomb2 = Piece("Bom", BOMB_POWER, START_X, START_Y)   
    Bomb3 = Piece("Bom", BOMB_POWER, START_X, START_Y)  
    Bomb4 = Piece("Bom", BOMB_POWER, START_X, START_Y)
    Bomb5 = Piece("Bom", BOMB_POWER, START_X, START_Y)       
    Bomb6 = Piece("Bom", BOMB_POWER, START_X, START_Y)
    p1.append(Bomb1)
    p1.append(Bomb2)
    p1.append(Bomb3)
    p1.append(Bomb4)
    p1.append(Bomb5)
    p1.append(Bomb6)
    
  
    #MARSHALL
    Marshall = Piece("Msh", MARSHALL_POWER, START_X, START_Y) 
    p1.append(Marshall)
    
    #GENERAL
    General = Piece("Gen", GENERAL_POWER,START_X,START_Y)
    p1.append(General)
    
    #COLONELs
    Colonel1 = Piece("Col", COLONEL_POWER, START_X, START_Y)
    Colonel2 = Piece("Col", COLONEL_POWER, START_X, START_Y)
    p1.append(Colonel1)
    p1.append(Colonel2)
    
    #MAJORS
    Major1 = Piece("Maj", MAJOR_POWER, START_X, START_Y)
    Major2 = Piece("Maj", MAJOR_POWER, START_X, START_Y)
    Major3 = Piece("Maj", MAJOR_POWER, START_X, START_Y)
    p1.append(Major1)
    p1.append(Major2)
    p1.append(Major3)
    
    #CAPTAINS
    Captain1 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y)
    Captain2 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y)
    Captain3 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y)
    Captain4 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y)
    p1.append(Captain1)
    p1.append(Captain2)
    p1.append(Captain3)
    p1.append(Captain4)

    #LIEUTENANTS
    Lieutenant1 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y)
    Lieutenant2 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y)
    Lieutenant3 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y)
    Lieutenant4 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y)
    p1.append(Lieutenant1)
    p1.append(Lieutenant2)
    p1.append(Lieutenant3)
    p1.append(Lieutenant4)
    
    #SERGEANTS
    Sergeant1 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y)
    Sergeant2 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y)
    Sergeant3 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y)
    Sergeant4 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y)
    p1.append(Sergeant1)
    p1.append(Sergeant2)
    p1.append(Sergeant3)
    p1.append(Sergeant4)
    
    #MINERS
    Miner1 = Piece("Min", MINER_POWER, START_X, START_Y)
    Miner2 = Piece("Min", MINER_POWER, START_X, START_Y)
    Miner3 = Piece("Min", MINER_POWER, START_X, START_Y)
    Miner4 = Piece("Min", MINER_POWER, START_X, START_Y)
    Miner5 = Piece("Min", MINER_POWER, START_X, START_Y)
    p1.append(Miner1)
    p1.append(Miner2)
    p1.append(Miner3)
    p1.append(Miner4)
    p1.append(Miner5)
    
    #SCOUTS
    Scout1 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout2 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout3 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout4 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout5 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout6 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout7 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    Scout8 = Piece("Sct", SCOUT_POWER, START_X, START_Y)
    p1.append(Scout1)
    p1.append(Scout2)
    p1.append(Scout3)
    p1.append(Scout4)
    p1.append(Scout5)
    p1.append(Scout6)
    p1.append(Scout7)
    p1.append(Scout8)
    
    #SPY
    Spy = Piece("Spy", SPY_POWER, START_X, START_Y)
    p1.append(Spy)
    
    return p1
        
def main():
    p1Graveyard = []
    p2Graveyard = []
    
    p1Pieces = initPieces()
    p2Pieces = initPieces()   
    
    p1Pieces[4].setPosition(8,7)
    p1Pieces[5].setPosition(8,8)
    p1Pieces[6].setPosition(7,7)
    p1Pieces[7].setPosition(7,8)
    
    p1Pieces[35].setPosition(5,8)


    
    createGrid()
    
    print (placePiece(p1Pieces[4]))
    print (placePiece(p1Pieces[5]))
    print (placePiece(p1Pieces[6]))
    print (placePiece(p1Pieces[7]))
    print (placePiece(p1Pieces[35]))

    
    
    printGrid()

    #P1 = Piece("General", 10, 5, 7)
    #placePiece(P1)
    
      
        
main()