from Piece import Piece
from persistent import Persistent
from Player import Player
import uuid

class Game(Persistent):

    def __init__():
        pass
    def __init__(self, whitePlayer:Player, blackPlayer:Player):
        self.gameId = str(uuid.uuid4())
        self.blackPlayer = blackPlayer
        self.whitePlayer=whitePlayer
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.blackPlayer.pieces=self.initializeBlackPieces()
        self.whitePlayer.pieces=self.initializeWhitePieces()
        self.whiteKing=(4,0)
        self.blackKing=(4,7)
 
    def printBoard(self):
        
        transposed_matrix = list(zip(*self.board))

        # for row in reversed(transposed_matrix):
        #     for item in reversed(row):
        #         print(item, end=' ')    
        #     print()  
        result = []
        for row in reversed(transposed_matrix):
            row_list = []
            for item in reversed(row):
                row_list.append(str(item))
            result.append(row_list)
        return result

    def initializeBlackPieces(self):
        pawn1=Piece(1,6,(0,6),"black",self.blackPlayer.id)
        self.board[0][6]=pawn1
        pawn2=Piece(2,6,(1,6),"black",self.blackPlayer.id)
        self.board[1][6]=pawn2
        pawn3=Piece(3,6,(2,6),"black",self.blackPlayer.id)
        self.board[2][6]=pawn3
        pawn4=Piece(4,6,(3,6),"black",self.blackPlayer.id)
        self.board[3][6]=pawn4
        pawn5=Piece(5,6,(4,6),"black",self.blackPlayer.id)
        self.board[4][6]=pawn5
        pawn6=Piece(6,6,(5,6),"black",self.blackPlayer.id)
        self.board[5][6]=pawn6
        pawn7=Piece(7,6,(6,6),"black",self.blackPlayer.id)
        self.board[6][6]=pawn7
        pawn8=Piece(8,6,(7,6),"black",self.blackPlayer.id)
        self.board[7][6]=pawn8

        rook1=Piece(9,3,(0,7),"black",self.blackPlayer.id)
        self.board[0][7]=rook1
        rook2=Piece(10,3,(7,7),"black",self.blackPlayer.id)
        self.board[7][7]=rook2


        bishop1=Piece(11,5,(2,7),"black",self.blackPlayer.id)
        self.board[2][7]=bishop1
        bishop2=Piece(12,5,(5,7),"black",self.blackPlayer.id)
        self.board[5][7]=bishop2
        knight1=Piece(13,4,(1,7),"black",self.blackPlayer.id)
        self.board[1][7]=knight1
        knight2=Piece(14,4,(6,7),"black",self.blackPlayer.id)
        self.board[6][7]=knight2

        king=Piece(15,1,(3,7),"black",self.blackPlayer.id)
        self.board[3][7]=king
        queen=Piece(16,2,(4,7),"black",self.blackPlayer.id)
        self.board[4][7]=queen

        blackPieces=[pawn1,pawn2,pawn3,pawn4,pawn5,pawn6,pawn7,pawn8,
                    rook1,rook2,bishop1,bishop2,knight1,knight2,king,queen]

        return blackPieces

    def initializeWhitePieces(self):
            wpawn1=Piece(17,6,(0,1),"white",self.whitePlayer.id)
            self.board[0][1]=wpawn1
            wpawn2=Piece(18,6,(1,1),"white",self.whitePlayer.id)
            self.board[1][1]=wpawn2
            wpawn3=Piece(19,6,(2,1),"white",self.whitePlayer.id)
            self.board[2][1]=wpawn3
            wpawn4=Piece(20,6,(3,1),"white",self.whitePlayer.id)
            self.board[3][1]=wpawn4
            wpawn5=Piece(21,6,(4,1),"white",self.whitePlayer.id)
            self.board[4][1]=wpawn5
            wpawn6=Piece(22,6,(5,1),"white",self.whitePlayer.id)
            self.board[5][1]=wpawn6
            wpawn7=Piece(23,6,(6,1),"white",self.whitePlayer.id)
            self.board[6][1]=wpawn6
            wpawn8=Piece(24,6,(7,1),"white",self.whitePlayer.id)
            self.board[7][1]=wpawn7

            wrook1=Piece(25,3,(0,0),"white",self.whitePlayer.id)
            self.board[0][0]=wrook1
            wrook2=Piece(26,3,(7,0),"white",self.whitePlayer.id)
            self.board[7][0]=wrook2

            wbishop1=Piece(27,5,(2,0),"white",self.whitePlayer.id)
            self.board[2][0]=wbishop1
            wbishop2=Piece(28,5,(5,0),"white",self.whitePlayer.id)
            self.board[5][0]=wbishop2

            wknight1=Piece(29,4,(1,0),"white",self.whitePlayer.id)
            self.board[1][0]=wknight1
            wknight2=Piece(30,4,(6,0),"white",self.whitePlayer.id)
            self.board[6][0]=wknight2

            wking=Piece(31,1,(3,0),"white",self.whitePlayer.id)
            self.board[3][0]=wking
            wqueen=Piece(32,2,(4,0),"white",self.whitePlayer.id)
            self.board[4][0]=wqueen

            whitePieces=[wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,
                        wrook1,wrook2,wbishop1,wbishop2,wknight1,wknight2,wking,wqueen]

            return whitePieces
    

    def showPossibleMoves(self, piece):
        moves=piece.defineMoves(piece.currentPosition)
        print(moves)
        movesFinal=[]
        #kralj ne sme drugog kralja
        #da li kralj moze da se pomeri i sam sebe stavi u mat 
        #KING
        if(piece.pieceTypeId==1):
            for item in moves:
                if(self.board[item[0]][item[1]]==None and not(piece.currentPosition[0]+2==item[0] or 
                                                              piece.currentPosition[0]-2==item[0])):

                    movesFinal.append(item)

                elif(self.board[item[0]][item[1]]!=None and not(piece.currentPosition[0]+2==item[0] or 
                                                              piece.currentPosition[0]-2==item[0])):
                    p:Piece
                    p=self.board[item[0]][item[1]]
                    if(p.color != piece.color):
                        movesFinal.append(item)

                #kingside castling, queenside castling
                elif piece.moved==False:
                    flag=False
                    if self.board[0][piece.currentPosition[1]].moved==False and item[0]==3:
                        for i in range(1,4):
                            if(self.board[i][piece.currentPosition[1]]!=None):
                                flag=True

                        if flag==False:
                            movesFinal.append(item)

                    flag=False
                    if self.board[7][piece.currentPosition[1]].moved==False and item[0]==5:
                        for i in range(5,7):
                            if(self.board[i][piece.currentPosition[1]]!=None):
                                flag=True

                        if flag==False:
                            movesFinal.append(item)

               


        #QUEEN    
        elif(piece.pieceTypeId==2):
        #left-up
            for item in moves:
                if(item[0]<piece.currentPosition[0] and item[1]>piece.currentPosition[1]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break 
                    break  
        #left-down
            for item in moves:
                    if(item[0]<piece.currentPosition[0] and item[1]<piece.currentPosition[1]):
                        if(self.board[item[0]][item[1]]==None):
                            movesFinal.append(item)
                        else:
                            p=self.board[item[0]][item[1]]
                            if(p.color != piece.color):
                                movesFinal.append(item)
                                break
                        break
        #right-up
            for item in moves:
                    if(item[0]>piece.currentPosition[0] and item[1]>piece.currentPosition[1]):
                        if(self.board[item[0]][item[1]]==None):
                            movesFinal.append(item)
                        else:
                            p=self.board[item[0]][item[1]]
                            if(p.color != piece.color):
                                movesFinal.append(item)
                                break
                        break
        #right-down        
            for item in moves:
                    if(item[0]>piece.currentPosition[0] and item[1]<piece.currentPosition[1]):
                        if(self.board[item[0]][item[1]]==None):
                            movesFinal.append(item)
                        else:
                            p=self.board[item[0]][item[1]]
                            if(p.color != piece.color):
                                movesFinal.append(item)
                                break 
                        break
        #left
            for item in moves:
                if(item[0]<piece.currentPosition[0]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break  
                    break              
        #right
            for item in moves:
                if(item[0]>piece.currentPosition[0]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break  
                    break          
        #up
            for item in moves:
                if(item[1]>piece.currentPosition[1]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break     
                    break       
        #down
            for item in moves:
                if(item[1]<piece.currentPosition[1]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break
                    break

        #ROOK
        elif(piece.pieceTypeId==3):
            #left
            for item in moves:
                if(item[0]<piece.currentPosition[0]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break  
                    break              
            #right
            for item in moves:
                if(item[0]>piece.currentPosition[0]):
                    if(self.board[item[0]][item[1]]==None):
                        print()
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            print("2")
                            movesFinal.append(item)
                            break   
                    break        

                        
            #up
            for item in moves:
                if(item[1]>piece.currentPosition[1]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                        print("1")
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            print("2")
                            break
                    break            
            #down
            for item in moves:
                if(item[1]<piece.currentPosition[1]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break
                    break
            
        #KNIGHT
        elif(piece.pieceTypeId==4):
            for item in moves:
                if(self.board[item[0]][item[1]]==None):
                    movesFinal.append(item)
                else:
                    p:Piece
                    p=self.board[item[0]][item[1]]
                    if(p.color != piece.color):
                        movesFinal.append(item)
        
        #BISHOP
        elif(piece.pieceTypeId==5):
        #left-up
            for item in moves:
                if(item[0]<piece.currentPosition[0] and item[1]>piece.currentPosition[1]):
                    if(self.board[item[0]][item[1]]==None):
                        movesFinal.append(item)
                    else:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                            break   
                    break
        #left-down
            for item in moves:
                    if(item[0]<piece.currentPosition[0] and item[1]<piece.currentPosition[1]):
                        if(self.board[item[0]][item[1]]==None):
                            movesFinal.append(item)
                        else:
                            p=self.board[item[0]][item[1]]
                            if(p.color != piece.color):
                                movesFinal.append(item)
                                break
                        break
        #right-up
            for item in moves:
                    if(item[0]>piece.currentPosition[0] and item[1]>piece.currentPosition[1]):
                        if(self.board[item[0]][item[1]]==None):
                            movesFinal.append(item)
                        else:
                            p=self.board[item[0]][item[1]]
                            if(p.color != piece.color):
                                movesFinal.append(item)
                                break
                        break
        #right-down        
            for item in moves:
                    if(item[0]>piece.currentPosition[0] and item[1]<piece.currentPosition[1]):
                        if(self.board[item[0]][item[1]]==None):
                            movesFinal.append(item)
                        else:
                            p=self.board[item[0]][item[1]]
                            if(p.color != piece.color):
                                movesFinal.append(item)
                                break  
                        break          
        
        #an pasan
        #PAWN  
        else:
            for item in moves:
                #can it move two squares forward
                if(piece.currentPosition[1]==item[1]+2 and piece.currentPosition[1]==1 and piece.color=="white"):
                    movesFinal.append(item)
                elif(piece.currentPosition[1]==item[1]-2 and piece.currentPosition[1]==6 and piece.color=="black"):
                    movesFinal.append(item)
        
                else:
                    #Can it eat a figure, including both diagonally and horizontally
                    if(piece.currentPosition[0]!=item[0] or piece.currentPosition[1]==item[1])  and self.board[item[0]][item[1]]!=None:
                        p=self.board[item[0]][item[1]]
                        if(p.color != piece.color):
                            movesFinal.append(item)
                    elif self.board[item[0]][item[1]]==None and piece.currentPosition[0]==item[0]:
                          movesFinal.append(item)

        #removing positions that would put us in check position
        movesFinalFinal=[]
        cp=piece.currentPosition          
        for m in movesFinal:
            piece.currentPosition=m
            check=self.checkCheck(piece)
            if piece.color=="white" and check[1]==0:
                movesFinalFinal.append(m)
            elif piece.color=="black" and check[0]==0:
                movesFinalFinal.append(m)

        piece.currentPosition=cp

        return movesFinalFinal
    
    def checkCheck(self):
        #0,0 - no checks
        #1,0 - white checks black 
        #0,1 - black checks white
        check=(0,0)

        for pc in self.whitePlayer.getPieces:
            if pc.isDead==False:
                moves=self.showPossibleMoves(pc)
                for m in moves:
                    if m==self.blackKing:
                        check[0]=1    

        for pc in self.blackPlayer.getPieces:
            if pc.isDead==False:
                moves=self.showPossibleMoves(pc)
                for m in moves:
                    if m==self.whiteKing:
                        check[1]=1

        return check 


    def checkCheckmate(self,piece):
        if(piece.color=="white"):
            for pc in self.blackPlayer.getPieces:
                moves=self.showPossibleMoves(pc)
                if len(moves)>0:
                    return False    
        else:
            for pc in self.whitePlayer.getPieces:
                moves=self.showPossibleMoves(pc)
                if len(moves)>0:
                    return False         
        return True
    

    def makeMove(self,piece,*nextPosition):
        #nextPosition se uzima sa fronta!!
        #check who's turn by taking the log from the database
        #postavljena je vrednost white samo da ne bi bacalo gresku
        nextMove="white"
        if(nextMove==piece.color):
            #checking if there is a castling and if so, moving the rook
            if piece.pieceTypeId==1 and nextPosition[0]==piece.currentPosition[0]+2:
                self.board[nextPosition[0]][nextPosition-1]=self.board[piece.currentPosition[0]][7]
                self.board[piece.currentPosition[0]][7]=None
            elif piece.pieceTypeId==1 and nextPosition[0]==piece.currentPosition[0]-2:
                self.board[nextPosition[0]][nextPosition+1]=self.board[piece.currentPosition[0]][0]
                self.board[piece.currentPosition[0]][0]=None
            #removing piece out of the game
            if(self.board[piece.nextPosition[0]][piece.nextPosition[1]])!=None:
                self.board[piece.nextPosition[0]][piece.nextPosition[1]].removePiece()
            #changing board
            self.board[piece.currentPosition[0]][piece.currentPosition[1]]=None
            self.board[nextPosition[0]][nextPosition[1]]=piece
            #updating position of the piece
            piece.movePiece(*nextPosition)
            #checking if the king was moved and in that case updating his position
            if(piece.pieceTypeId==1):
                if(piece.color=="white"):
                    self.whiteKing=(nextPosition[0],nextPosition[1])
                else:
                    self.blackKing=(nextPosition[0],nextPosition[1])
            #checking if the pawn has reached the end of the board
            if piece.pieceTypeId==6 and (nextPosition[1]==7 or nextPosition[1]==0):
                #uzimamo sa fronta novi tip, moze biti kraljica,top, lovac,konj
                #za kraljicu se vraca 2, za topa 3, za konja 4 i za lovca 5
                piece.swapPieceType(2)
            #checking if there is a check or checkmate
            check=self.checkCheck()
            if check:
                checkmate=self.checkCheckmate()
                if checkmate:
                    #game end
                    pass
            #putting the log into the database

       
        


#ovo smo mi koristile za proveru, probaj i ti tako
# p1=Player(1,"Milica",None)
# p2=Player(2,"Ana",None)
# p = Piece(32,2,(0,4),"white",1)
# g=Game(1,p1,p2)
# g.printBoard()
# print(p1.getPieces()[0])
# pm=g.showPossibleMoves(p1.getPieces()[0])
# print(pm)