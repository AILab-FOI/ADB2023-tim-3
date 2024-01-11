from flask import Flask
from flask_socketio import SocketIO, join_room

#povezivanje preko soketa - nije zavrseno

app = Flask(__name__)
socketio = SocketIO(app)

games = {}

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('create_game')
def create_game():
    game_id = str(hash(socketio.sid))  # Use a more robust method for generating unique game IDs
    games[game_id] = {'players': [socketio.sid]}
    join_room(game_id)
    socketio.emit('game_created', {'game_id': game_id})

@socketio.on('join_game')
def join_game(data):
    game_id = data['game_id']
    
    if game_id in games and len(games[game_id]['players']) < 2:
        join_room(game_id)
        games[game_id]['players'].append(socketio.sid)
        socketio.emit('game_joined', {'game_id': game_id})
    else:
        socketio.emit('game_full', {'game_id': game_id})

if __name__ == '__main__':
    socketio.run(app)