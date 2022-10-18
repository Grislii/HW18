from flask import request, jsonify
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        rq_director_id = request.values.get('director_id')
        rq_genre_id = request.values.get('genre_id')
        rq_year = request.values.get('year')

        if rq_director_id is None and rq_genre_id is None and rq_year is None:
            all_movies = movie_service.get_all()
            return jsonify(movies_schema.dump(all_movies))
        elif rq_director_id is not None:
            movies = movie_service.get_all_with_director(rq_director_id)
            return jsonify(movies_schema.dump(movies))
        elif rq_genre_id is not None:
            movies = movie_service.get_all_with_genre(rq_genre_id)
            return jsonify(movies_schema.dump(movies))
        elif rq_year is not None:
            movies = movie_service.get_all_with_year(rq_year)
            return jsonify(movies_schema.dump(movies))

    def post(self):
        rq_json = request.json
        movie_service.create(rq_json)
        return "Фильм успешно добавлен", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        rq_json = request.json
        movie_service.update(rq_json, mid)
        return "Фильм успешно обновлён", 201

    def delete(self, mid):
        movie_service.delete(mid)
        return "Фильм успешно удалён", 200
