from ZODB import DB
from ZEO.ClientStorage import ClientStorage
import transaction
from typing import List
import threading
from persistent.mapping import PersistentMapping

lock = threading.Lock()

def getLogsByGameId(gameId):
    with lock:
        logs = []
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            valid_game_id = False
            game_keys = root['games'].keys()
            for key in game_keys:
                if key == gameId:
                    valid_game_id = True
            if valid_game_id == True:
                for log_entry in root['logs'].keys():
                    parts = log_entry.split('_')
                    id = parts[0]
                    if id == gameId:
                        root['logs'][log_entry].turnNo
                        logs.append(root['logs'][log_entry])
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
            valid_game_id = False
            game_keys = root['games'].keys()
            for key in game_keys:
                if key == gameId:
                    valid_game_id = True
            if valid_game_id == True:
                object_name = str(gameId)+'_log_'+str(turnNo)
                log = root['logs'][object_name]
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
        games = root['games'].values()

        try:
            for game in games:
                if game.gameId == gameId:
                    return game
        except Exception as e:
            print(f"Error while reading object game: {e}")
        finally:
            connection.close()
            db.close()

def getPlayer(playerName, gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            object_name = str(gameId)+'_player_'+str(playerName)
            player = root['players'][object_name]
            player.id
        except Exception as e:
            print(f"Error while reading object {playerName}: {e}")
        finally:
            connection.close()
            db.close()

        return player

def getPiece(pieceName, gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            object_name = str(gameId)+'_piece_'+str(pieceName)
            piece = root['pieces'][object_name]
            piece.color
        except Exception as e:
            print(f"Error while reading object {pieceName}: {e}")
        finally:
            connection.close()
            db.close()

        return piece

def getPieceTypes():
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        try:
            pieceTypes = list(root['piece_types'].values())
            pieceTypes[0].typeid
        except Exception as e:
            print(f"Error while reading object pieceType: {e}")
        finally:
            connection.close()
            db.close()

        return pieceTypes

def addLog(log, gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()
        
        try:
            valid_game_id = False
            game_keys = root['games'].keys()
            for key in game_keys:
                if key == gameId:
                    valid_game_id = True
            if valid_game_id == True:
                with transaction.manager:
                    object_name = str(gameId)+'_log_'+str(log.turnNo)
                    root['logs'][object_name] = log

                print("New Log entry added to the database")
            else:
                print("Given invalid game id")
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

        try:
            if 'games' not in root:
                with transaction.manager:
                    root['games'] = PersistentMapping()
                    root['logs'] = PersistentMapping()
                    root['players'] = PersistentMapping()
                    root['pieces'] = PersistentMapping()
                    root['piece_types'] = PersistentMapping()

            with transaction.manager:
                root['games'][game.gameId] = game
            
            print("Game with id", game.gameId, "added to the database")
            
        except Exception as e:
            print(f"Error during transaction: {e}")
            transaction.abort()
        finally:
            connection.close()
            db.close()

def addPlayer(player, gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        with transaction.manager:
            object_name = str(gameId)+'_player_'+str(player.name)
            root['players'][object_name] = player
        
        print(player.name, "added to the database")

        connection.close()
        db.close()

def addPieces(pieces:List[any], namesOfPieces, gameId):
    with lock:
        storage = ClientStorage( ( 'localhost', 8090 ) )
        db = DB(storage)
        connection = db.open()
        root = connection.root()

        for i, piece in enumerate(pieces):
            with transaction.manager:
                object_name = str(gameId)+'_piece_'+str(namesOfPieces[i])
                root['pieces'][object_name] = piece

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
                root['piece_types'][pieceType.typename] = pieceType

        print("Piece types added to the database")

        connection.close()
        db.close()
