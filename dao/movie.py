from dao.model.movie import Movie
from setup_db import db


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()

    def get_all_with_director(self, mid):
        with db.session.begin():
            query = db.session.query(Movie).filter(Movie.director_id == mid).all()
        return query

    def get_all_with_genre(self, mid):
        with db.session.begin():
            query = db.session.query(Movie).filter(Movie.genre_id == mid).all()
        return query

    def get_all_with_year(self, mid):
        with db.session.begin():
            query = db.session.query(Movie).filter(Movie.year == mid).all()
        return query
