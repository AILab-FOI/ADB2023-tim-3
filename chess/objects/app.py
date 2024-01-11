from flask import Flask,Response
from Game import Game
from Player import Player
from Piece import Piece
from flask import jsonify, request

app = Flask("__name__")

p1=Player(0,"",None)
p2=Player(0,"",None)
g = Game(0, None, None)
#p1:Player
#p2:Player
#g = Game(1,p1,p2)
#p = Piece(32,2,(0,4),"white",1)

@app.route("/igraci", methods = ['POST'])
def getNames():
    data = request.get_json() 
    name1 = ''
    name2 = ''
    gameid = -1


    if 'name1' in data:
        name1 = data['name1']
    if 'name2' in data:
        name2 = data['name2'] 
    if 'gameid' in data:
        gameid = data['gameid']    

    #umesto ovoga se prave objekti plejera koji se ubacuju u bazu
     #da li ce se slati i id igre koji unose? Ako se salje, da li ce se na frontu proveravati plejeri koji su uneli isti id ili se to radi na beku
        
    p1.id = 1
    p1.name = name1
    p2.id = 2
    p2.name = name2
    #Ubaciti game u bazu - name 1 je plejer koji prvi igra
    g.gameId = gameid
    g.whitePlayer = p1
    g.blackPlayer = p2
     

    print(f"Ime prvog igraca je: {p1.name}, a ime drugog je: {p2.name}")
    
    return Response(status=200)

  #treba da se zapocne igra - uzeti podatke koji se dobijaju pokretanjem konstruktora  
  #treba da uzmemo figuru sa fronta i za nju da vratimo possibleMoves  
  #treba da uzmemo nextPosition i da pozovemo makeMove i vratimo novi board
  #treba da uzmemo za koju figuru se pawn menja
  #treba da posaljemo da li je sah/sah mat


# @app.route("/board")
# def prikaziBoard():   
#     return jsonify(g.printBoard())

@app.route("/home")
def home():
    return f"Ime jeeeeeeeeeeeeeeeeeee {p1.name}"

if __name__ == "__main__":
    app.run(host = "localhost", port = 5004)