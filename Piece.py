



class Piece():
    type = None   #Piece types, Lake, Nothing, etc.
    power = None
    posX = None
    posY = None
    
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


column = [] * 10

def placePiece(P1):
    x = P1.getPosition()
    column[x[1]][x[0]] = P1
    #Creates a 10x10 Grid
def createGrid():
    for i in range(10):
        row = [Piece] * 10
        ch = 'A'
        x = chr(ord(ch) + i)
        for j in range(10):
            row[j] = "--"
        column[i] = row

        
    column[4][2] = "[]"
    column[4][3] = "[]"
    column[5][2] = "[]"
    column[5][3] = "[]"
 

    column[4][6] = "[]"
    column[4][7] = "[]"
    column[5][6] = "[]"
    column[5][7] = "[]"
        


def initPieces(p1, p2):
    General1 = Piece("General", 10,0,0)
    General2 = Piece("General", 10,0,0)
    
    p1.append(General1)
    p2.append(General2)
    
        
        
    print(column[3][5]) 
    for i in range(10):
        print(column[i]) 
        
def main():
    p1Pieces = []
    p2Pieces = []
    
    General1 = Piece("General", 10,0,0)
    General2 = Piece("General", 10,0,0)
    
    print(General1.getType())
    
    
    #createGrid()
    #P1 = Piece("General", 10, 5, 7)
    #placePiece(P1)
        
        
main()