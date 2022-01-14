from flask import Flask
from flask import request
from flask import jsonify

from playhouse.shortcuts import model_to_dict, dict_to_model

from peewee import *

db = PostgresqlDatabase('hungarian_films', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
	class Meta:
		database = db

class Films(BaseModel):
	title_en = CharField()
	title_hu = CharField()
	year = IntegerField()
	was_banned = BooleanField()
	directed_by = IntegerField()
	restored = BooleanField()
	is_documentary = BooleanField()


class Directors(BaseModel):
	director_id = IntegerField()
	name = CharField()
	birth = CharField()

db.connect()

app = Flask(__name__)

@app.route('/films', methods=['GET'])
@app.route('/films/<id>', methods=['GET'])
def film(id=None):
	if request.method == 'GET':
		if id:
			film = Films.get(Films.id == id)
			film = model_to_dict(film)
			film = jsonify(film)
			return film
		else:
			films = []
			for film in Films.select():
				film = model_to_dict(film)
				films.append(film)
			films = jsonify(films)
			return films

	if request.method == 'POST':
		film = request.get_json()
		film = dict_to_model(Film, film)
		film.save()
		film = dict_to_model(film)
		film = jsonify(film)
		return jsonify(film)

	if request.method == 'DELETE':
		film = Film.get(Film.id == id)
		film.delete_instance()
		return jsonify({'deleted' : True})

	if request.method == 'PUT':
		updated_film = request.get_json()
		film = Film.get(Film.id == id)
		film['title_en'] = updated_film['title_en']
		# ect.
		film.save()
		film = model_to_dict(film)
		film = jsonify(film)
		return film


@app.route('/directors', methods=['GET'])
def directors(id=None):
	if request.method == 'GET':
		if id:
			director = Directors.get(Director.id == id)
			director = model_to_dict(director)
			director = jsonify(director)
			return director
		else:
			directors = []
			for director in Directors.select():
				director = directors.append(model_to_dict(director))
				directors.append(director)
			directors = jsonify(directors)
			return directors

	if request.method == 'POST':
		director = request.get_json()
		director = dict_to_model(Director, director)
		film.save()
		director = dict_to_model(director)
		director = jsonify(director)
		return jsonify(director)


app.run(port=9000, debug=True)

