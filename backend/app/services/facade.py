from app.persistence.repository import SQLAlchemyRepository
from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.amenity_repository import AmenityRepository
from app.services.repositories.review_repository import ReviewRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()

    # User method
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute(email)

    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)
        return self.user_repo.get(user_id)
    
    def get_all_users(self):
         return self.user_repo.get_all()

    # Profession method
    def create_profession(self, profession_data):
        profession = Profession(**profession_data)
        self.profession_repo.add(profession)
        return profession

    def get_profession(self, profession_id):
        return self.profession_repo.get(profession_id)

    def get_all_professions(self):
        return self.profession_repo.get_all()

    def update_profession(self, profession_id, profession_data):
        self.profession_repo.update(profession_id, profession_data)
        return self.profession_repo.get(profession_id)
    
    def delete_profession(self, profession_id):
        self.profession_repo.delete(profession_id)
        return self.profession_repo.get_all()

    # Review Methode
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_porfession(self, profession_id):
        return self.review_repo.get_all_by_attribute('profession_id', profession_id)

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
        return self.review_repo.get_all()
