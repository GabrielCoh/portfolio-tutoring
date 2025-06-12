from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review
from app import db
from app.persistence.repository import SQLAlchemyRepository
from flask import has_app_context

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)
        
        
    def add(self, profession):
        db.session.add(profession)
        db.session.commit()
        return profession
    
    def update(self, profession_id, profession_data):
        profession = Profession.query.get(profession_id)
        profession.update(profession_data)
        db.session.commit()
        return profession

    def delete(self, profession_id):
        profession = self.get(profession_id)
        if profession:
            Review.query.filter(Review.profession_id == profession_id).delete(synchronize_session=False)
            
            db.session.delete(profession)
            db.session.commit()
        
    def get_profession(profession_id, options=None):
        profession = Profession.query.filter_by(id=profession_id)
        if options:
            profession = profession.options(*options)
        return profession.first()
