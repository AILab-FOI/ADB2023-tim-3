from ZODB import DB
from ZEO.ClientStorage import ClientStorage
import transaction
from typing import List
import threading

lock = threading.Lock()

def getLogsByGameId(gameId):
    with lock:
        logs = []
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            game = root[gameId]
            if game is not None:
                i = 1
                while True:
                    zapis = "log"+str(i)
                    log_entry = root[zapis] 
                    if  log_entry is not None:
                        log_entry.turnNo
                        logs.append(log_entry)
                        i = i + 1
                    else:
                        break
            else:
                print("Game with Id:", gameId, "not in the database")
        except Exception as e:
            print(f"Error while reading logs: {e}")
        finally:
            connection.close()
            db.close()
        return logs

def getLogByTurnNo(turnNo, gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            game = root[gameId]
            if game is not None:
                zapis = "log"+str(turnNo)
                log = root[zapis]
                log.turnNo
                return log
            else:
                print("Game with Id:", gameId, "not in the database")
        except Exception as e:
            print(f"Error while reading log: {e}")
        finally:
            connection.close()
            db.close()

def getGame(gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            game = root.get(gameId)
            if game:
                game.gameId
                game.whitePlayer.name
                game.blackPlayer.name
                game.board
        except Exception as e:
            print(f"Error while reading object game: {e}")
        finally:
            connection.close()
            db.close()

        return game

def getPlayer(playerName):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            player = root.get(playerName)
            if player:
                #print("Player", player.name, "read from database")
                player.id
                player.name
        except Exception as e:
            print(f"Error while reading object {playerName}: {e}")
        finally:
            connection.close()
            db.close()

        return player

def getPiece(pieceName):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            piece = root.get(pieceName)
            #if piece:
                #print("Piece", pieceName, "read from database")
        except Exception as e:
            print(f"Error while reading object {pieceName}: {e}")
        finally:
            connection.close()
            db.close()

        return piece

def getPieceType(pieceTypeName):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            pieceType = root.get(pieceTypeName)
            if pieceType:
                #print("Piece type", pieceType.typename, "read from database")
                pieceType.typeid
        except Exception as e:
            print(f"Error while reading object {pieceTypeName}: {e}")
        finally:
            connection.close()
            db.close()

        return pieceType

def addLog(log):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()
        
        try:
            zapis = "log"+str(log.turnNo)

            with transaction.manager:
                root[zapis] = log

            print("New Log entry added to the database")
        except Exception as e:
            print(f"Error while adding log: {e}")
            transaction.abort()
        finally:
            connection.close()
            db.close()

def addGame(game):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        with transaction.manager:
            root[game.gameId] = game

        print("Game with id", game.gameId, "added to the database")

        connection.close()
        db.close()

def addPlayer(player):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        with transaction.manager:
            root[player.name] = player
        
        print(player.name, "added to the database")

        connection.close()
        db.close()

def addPieces(pieces:List[any], namesOfPieces):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        for i, piece in enumerate(pieces):
            with transaction.manager:
                root[namesOfPieces[i]] = piece

        print("Pieces added to the database")

        connection.close()
        db.close()

def addPieceTypes(pieceTypes:List[any]):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        for pieceType in pieceTypes:
            with transaction.manager:
                root[pieceType.typename] = pieceType

        print("Piece types added to the database")

        connection.close()
        db.close()
