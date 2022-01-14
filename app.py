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

@app.route('/films', methods=['GET', 'POST'])
@app.route('/films/<id>', methods=['GET', 'PUT', 'DELETE'])
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
		film = dict_to_model(Films, film)
		film.save()
		film = dict_to_model(film)
		film = jsonify(film)
		return jsonify(film)

	if request.method == 'DELETE':
		film = Films.get(Films.id == id)
		film.delete_instance()
		return jsonify({'deleted' : True})

	if request.method == 'PUT':
		updated_film = request.get_json()
		film = Films.get(Films.id == id)
		film['title_en'] = updated_film['title_en']
		film['title_hu'] = updated_film['title_hu']
		film['year'] = updated_film['year']
		film['was_Banned'] = updated_film['was_banned']
		film['directed_by'] = updated_film['directed_by']
		film['is_documentary'] = updated_film['is_documentary']
		film['restored'] = updated_film['restored']
		film.save()
		film = model_to_dict(film)
		film = jsonify(film)
		return film

@app.route('/films/banned', methods=['GET'])
def banned_films():
	films =[]
	for film in Films.select().where(Films.was_banned == True):
		film = model_to_dict(film)
		films.append(film)
	films = jsonify(films)
	return films

@app.route('/films/documentary', methods=['GET'])
def documentary_films():
	films =[]
	for film in Films.select().where(Films.was_banned == True):
		film = model_to_dict(film)
		films.append(film)
	films = jsonify(films)
	return films


@app.route('/directors', methods=['GET', 'POST'])
@app.route('/directors/<id>', methods=['GET', 'DELETE', 'PUT'])
@app.route('/directors/films/<directorid>', methods=['GET'])
def directors(id=None, directorid=None):
	if request.method == 'GET':
		if id:
			director = Directors.get(Directors.id == id)
			director = model_to_dict(director)
			director = jsonify(director)
			return director
		elif directorid:
			directors_films = []
			for film in Films.select().join(Directors, on=(Directors.id == Films.directed_by)).where(Films.directed_by == directorid):
				film = model_to_dict(film)
				directors_films.append(film)
			directors_films = jsonify(directors_films)
			return directors_films
		else:
			directors = []
			for director in Directors.select():
				director = model_to_dict(director)
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

	if request.method == 'DELETE':
		director = Directors.get(Directors.id == id)
		director.delete_instance()
		return jsonify({'deleted' : True})

	if request.method == 'PUT':
		updated_director = request.get_json()
		director = Directors.get(Directors.id == id)
		director['name'] = updated_director['name']
		director['director_id'] = updated_director['director_id']
		director['year'] = updated_director['year']
		director.save()
		director = model_to_dict(director)
		director = jsonify(director)
		return director


app.run(port=9000, debug=True)

