from api.models.occupation import Occupation
from api import db


class OccupationRepository:

    @staticmethod
    def get_all_occupations():
        try:
            return Occupation.query.all()
        except:
            return []

    @staticmethod
    def add_occupation(occupation):
        try:
            db.session.add(occupation)
            db.session.commit()
        except Exception as err:
            print(err)
            return False
        return True

    @staticmethod
    def delete_occupation(id):
        try:
            Occupation.query.filter_by(id=id).delete()
            db.session.commit()
        except:
            return False
        return True

    @staticmethod
    def get_occupations_by_playa_id(playa_id):
        try:
            return Occupation.query.filter_by(playa_id=playa_id).all()
        except:
            return []

    @staticmethod
    def get_occupation_by_id(id):
        try:
            return Occupation.query.get(id)
        except:
            return None