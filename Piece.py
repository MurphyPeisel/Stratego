from constants import *
import arcade

class Piece():
    type = None
    power = None
    posX = None
    posY = None
    player = None
    defeated = False
    hidden = True
    
    def __init__ (self, type, power, x, y, player):        
        self.type = type
        self.power = power
        self.posX = x
        self.posY = y
        self.player = player
        self.hidden = True
    
    def getType(self):
        return self.type
    def getPower(self):
        return self.power
    def getPosition(self):
        pos = [self.posX, self.posY]
        return pos
    
    def getPlayer(self):
        return self.player
    def getHidden(self):
        return self.hidden
    
    def setHidden(self, hide):
        self.hidden = hide

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
        

def is_piece_scan_local(pieces, loc):
    """
    Checks if there is a piece at the location of a provided coordinate set, this is to be used inside the show
    available moves function so that it only returns the necessary values.
    :param pieces: List of all pieces
    :param loc: location to check for a piece (x, y)
    :return boolean value: This value represents whether there is a piece at the given location
    """
    x = loc[0]
    y = loc[1]
    for piece in pieces:
        piecex = piece.getPosition()[0]
        piecey = piece.getPosition()[1]
        if x>=BOARD_LEFT + BOARD_MARGIN*piecex and x<=BOARD_RIGHT + BOARD_MARGIN*piecex and y<= BOARD_TOP + BOARD_MARGIN*piecey and y>= BOARD_BOTTOM + BOARD_MARGIN*piecey:
            return True
    return False

def check_orthogonal(piece1, piece2, pieces):
    """ 
    Checks if two pieces are orthogonally adjacent.
    :param piece1: First piece
    :param piece2: Second piece
    :return: 'True' if orthongal, 'False' otherwise
    :rtype: bool
    """
    lake_piece_1 = Piece("Lke", 0, 2, 4, 3)
    lake_piece_2 = Piece("Lke", 0, 3, 4, 3)
    lake_piece_3 = Piece("Lke", 0, 2, 5, 3)
    lake_piece_4 = Piece("Lke", 0, 3, 5, 3)

    lake_piece_5 = Piece("Lke", 0, 6, 4, 3)
    lake_piece_6 = Piece("Lke", 0, 7, 4, 3)
    lake_piece_7 = Piece("Lke", 0, 6, 5, 3)
    lake_piece_8 = Piece("Lke", 0, 7, 5, 3)

    lakes = [lake_piece_1,lake_piece_2,lake_piece_3,lake_piece_4,lake_piece_5,lake_piece_6,lake_piece_7,lake_piece_8]
    x_diff = piece1.posX - piece2.posX
    y_diff = piece1.posY - piece2.posY
    if piece1.getType() == "Sct":
        # same column
        valid_move = True
        if x_diff == 0 and valid_move:
            if y_diff > 0:
                for cell in range(piece2.posY - 1, piece1.posY):
                    if is_piece_scan_local(pieces, (piece1.posX, cell)) != False:
                            valid_move = False
                    for lake in lakes:
                        if lake.getPosition() == [piece1.posX, cell]:
                            valid_move = False
            else:
                for cell in range(piece1.posY+1, piece2.posY):
                    if is_piece_scan_local(pieces, (piece1.posX, cell)) != False:
                        valid_move = False
                    for lake in lakes:
                        if lake.getPosition() == [piece1.posX, cell]:
                            valid_move = False
        # same row
        elif y_diff == 0 and valid_move:
            if x_diff > 0:
                for cell in range(piece2.posX + 1, piece1.posX):
                    if is_piece_scan_local(pieces, (cell, piece1.posY)) != False:
                        valid_move = False
                    for lake in lakes:
                        if lake.getPosition() == [cell, piece1.posY]:
                            valid_move = False
            else:
                for cell in range(piece1.posX+1, piece2.posX):
                    if is_piece_scan_local(pieces, (cell, piece1.posY)) != False:
                        valid_move = False
                    for lake in lakes:
                        if lake.getPosition() == [cell, piece1.posY]:
                            valid_move = False
        else:
            return False              

        if valid_move:
            return True
        else:
            return False
        
    elif (abs(x_diff) == 0 and abs(y_diff) == 1) or (abs(x_diff) == 1 and (y_diff) == 0):
        return True
    else:
        return False


#Initialize 40 pieces per player
def initPieces(player):
    p1 = []
    #FLAG
    Flag = Piece("Flg", NO_POWER, START_X, START_Y, player)
    p1.append(Flag)
  
    #MARSHAL
    Marshal = Piece("Msh", MARSHAL_POWER, START_X, START_Y, player) 
    p1.append(Marshal)
    
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
        
