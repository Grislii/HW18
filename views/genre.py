from flask import jsonify
from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return jsonify(genres_schema.dump(all_genres))


@genre_ns.route('/<int:mid>')
class GenreView(Resource):
    def get(self, mid):
        genre = genre_service.get_one(mid)
        return jsonify(genre_schema.dump(genre))
