from flask import Flask, jsonify, request
from models import db, User, Characters, Planets, Favorites
app = Flask(__name__)



@app.route('/people', methods=['GET'])
def get_people():
    json_text = Characters.query.all()
    results = list(map(lambda personajes: personajes.serialize(), Characters))    
    return jsonify(results), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_id(people_id):
    json_text = Characters.query.filter_by(id=people_id).first()
    results = json_text.serialize()    
    return jsonify(results), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    json_text = Planets.query.all()
    results = list(map(lambda planetas: planetas.serialize(), Planets))    
    return jsonify(results), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planets_id(planets_id):
    json_text = Planets.query.filter_by(id=planets_id).first()
    results = json_text.serialize()    
    return jsonify(results), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    json_text = User.query.filter_by(id=user_id).first()
    results = json_text.serialize()    
    return jsonify(results), 200

@app.route('/users', methods=['GET'])
def get_users():
    json_text = User.query.all()
    results = list(map(lambda usuarios: usuarios.serialize(), User))    
    return jsonify(results), 200

@app.route('/users/favorites', methods=['GET'])
def get_users_favorites():
    json_text = Favorites.query.all()
    results = list(map(lambda favoritos: favoritos.serialize(), Favorites))    
    return jsonify(results), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def favorite_planet_id():
    request_body = request.get_json(force=True)
    todos.append(request_body)    
    return jsonify(todos)

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def favorite_people_id():
    request_body = request.get_json(force=True)
    todos.append(request_body)    
    return jsonify(todos)

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(position):
    todos.pop(position)
    return jsonify(todos)

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(position):
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)