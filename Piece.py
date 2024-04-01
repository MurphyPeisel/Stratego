from constants import *
import arcade

class Piece():
    type = None   #Piece types, Lake, Nothing, etc.
    power = None
    posX = None
    posY = None
    player = None
    defeated = False
    
    def __init__ (self, type, power, x, y, player):        
        self.type = type
        self.power = power
        self.posX = x
        self.posY = y
        self.player = player

    
    def getType(self):
        return self.type
    def getPower(self):
        return self.power
    def getPosition(self):
        pos = [self.posX, self.posY]
        return pos
    
    def getPlayer(self):
        return self.player

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

def check_orthogonal(piece1, piece2):
    """ 
    Checks if two pieces are orthogonally adjacent.
    :param piece1: First piece
    :param piece2: Second piece
    :return: 'True' if orthongal, 'False' otherwise
    :rtype: bool
    """
    x_diff = abs(piece1.posX - piece2.posX)
    y_diff = abs(piece1.posY - piece2.posY) 
    if (x_diff == 0 and y_diff == 1) or (x_diff == 1 and y_diff == 0):
        return True
    else:
        return False

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
def initPieces(player):
    p1 = []
    #FLAG
    Flag = Piece("Flg", FLAG_POWER, START_X, START_Y, player)
    p1.append(Flag)
  
    #MARSHALL
    Marshall = Piece("Msh", MARSHALL_POWER, START_X, START_Y, player) 
    p1.append(Marshall)
    
    #GENERAL
    General = Piece("Gen", GENERAL_POWER,START_X,START_Y, player)
    p1.append(General)
    
    #COLONELs
    Colonel1 = Piece("Col", COLONEL_POWER, START_X, START_Y, player)
    Colonel2 = Piece("Col", COLONEL_POWER, START_X, START_Y, player)
    p1.append(Colonel1)
    p1.append(Colonel2)
    
    #MAJORS
    Major1 = Piece("Maj", MAJOR_POWER, START_X, START_Y, player)
    Major2 = Piece("Maj", MAJOR_POWER, START_X, START_Y, player)
    Major3 = Piece("Maj", MAJOR_POWER, START_X, START_Y, player)
    p1.append(Major1)
    p1.append(Major2)
    p1.append(Major3)
    
    #CAPTAINS
    Captain1 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y, player)
    Captain2 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y, player)
    Captain3 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y, player)
    Captain4 = Piece("Cap", CAPTAIN_POWER, START_X, START_Y, player)
    p1.append(Captain1)
    p1.append(Captain2)
    p1.append(Captain3)
    p1.append(Captain4)

    #LIEUTENANTS
    Lieutenant1 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y, player)
    Lieutenant2 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y, player)
    Lieutenant3 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y, player)
    Lieutenant4 = Piece("Ltn", LIEUTENANT_POWER, START_X, START_Y, player)
    p1.append(Lieutenant1)
    p1.append(Lieutenant2)
    p1.append(Lieutenant3)
    p1.append(Lieutenant4)
    
    #SERGEANTS
    Sergeant1 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y, player)
    Sergeant2 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y, player)
    Sergeant3 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y, player)
    Sergeant4 = Piece("Sgt", SERGEANT_POWER, START_X, START_Y, player)
    p1.append(Sergeant1)
    p1.append(Sergeant2)
    p1.append(Sergeant3)
    p1.append(Sergeant4)
    
    #MINERS
    Miner1 = Piece("Min", MINER_POWER, START_X, START_Y, player)
    Miner2 = Piece("Min", MINER_POWER, START_X, START_Y, player)
    Miner3 = Piece("Min", MINER_POWER, START_X, START_Y, player)
    Miner4 = Piece("Min", MINER_POWER, START_X, START_Y, player)
    Miner5 = Piece("Min", MINER_POWER, START_X, START_Y, player)
    p1.append(Miner1)
    p1.append(Miner2)
    p1.append(Miner3)
    p1.append(Miner4)
    p1.append(Miner5)
    
    #BOMBS
    Bomb1 = Piece("Bom", BOMB_POWER, START_X, START_Y, player)
    Bomb2 = Piece("Bom", BOMB_POWER, START_X, START_Y, player)   
    Bomb3 = Piece("Bom", BOMB_POWER, START_X, START_Y, player)  
    Bomb4 = Piece("Bom", BOMB_POWER, START_X, START_Y, player)
    Bomb5 = Piece("Bom", BOMB_POWER, START_X, START_Y, player)       
    Bomb6 = Piece("Bom", BOMB_POWER, START_X, START_Y, player)
    p1.append(Bomb1)
    p1.append(Bomb2)
    p1.append(Bomb3)
    p1.append(Bomb4)
    p1.append(Bomb5)
    p1.append(Bomb6)
    
    #SPY
    Spy = Piece("Spy", SPY_POWER, START_X, START_Y, player)
    p1.append(Spy)

    #SCOUTS
    Scout1 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout2 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout3 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout4 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout5 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout6 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout7 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    Scout8 = Piece("Sct", SCOUT_POWER, START_X, START_Y, player)
    p1.append(Scout1)
    p1.append(Scout2)
    p1.append(Scout3)
    p1.append(Scout4)
    p1.append(Scout5)
    p1.append(Scout6)
    p1.append(Scout7)
    p1.append(Scout8)
    
    return p1
        
