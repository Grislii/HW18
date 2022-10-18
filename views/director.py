from flask import jsonify
from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class GenreView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return jsonify(directors_schema.dump(all_directors)), 200


@director_ns.route('/<int:mid>')
class GenreView(Resource):
    def get(self, mid):
        director = director_service.get_one(mid)
        return jsonify(director_schema.dump(director)), 200
