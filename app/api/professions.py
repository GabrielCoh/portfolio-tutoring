from flask import jsonify
from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity
from doc_models import initialize_models

api = Namespace('professions', description='Profession operations')
models = initialize_models(api)

@api.route('/')
class ProfessionList(Resource):
    @api.expect(models['PlaceCreate'])
    @api.response(201, 'Profession successfully created', models['ProfessionResponse'])
    @api.response(400, 'Invalid input data', models['InvalidInput'])
    @api.response(403, 'Unauthorized action', models['UnauthorizedAction'])
    @jwt_required()
    @api.doc(security='token')
    def post(self):
        """Register a new profession"""
        current_user = get_jwt_identity().get('id')
        user = facade.get_user(current_user)
        
        if not user:
            api.abort(403, "Unauthorized action")

        profession_data = api.payload
        
        valid_inputs = ["title", "description", "price"]
        for input in place_data:
            if input not in valid_inputs:
                api.abort(400, f"Invalid input data: {input}")
        
        profession_data["owner_id"] = user.id

        try:    
            new_profession = facade.create_profession(profession_data)
            profession_dict = new_profession.to_dict()
        except (ValueError, TypeError) as e:
            api.abort(400, str(e))

        return profession_dict, 201

    @api.response(200, 'List of professions retrieved successfully', models['ProfessionsList'])
    def get(self):
        """Retrieve a list of all professions"""
        all_professions = facade.get_all_professions()
        professions_list = [profession.to_dict() for profession in all_professions]
        for place in places_list:
            reviews = facade.get_reviews_by_place(place.get("id"))
            if reviews:
                total_rating = sum(review.rating for review in reviews)
                total_reviews = len(reviews)
                profession["ratingAvg"] = total_rating / total_reviews
            else:
                profession["ratingAvg"] = 0
        return profession_list, 200

@api.route('/<profession_id>')
class ProfessionResource(Resource):
    @api.response(200, 'Profession details retrieved successfully', models['ProfessionByIdResponse'])
    @api.response(404, 'Profession not found', models['NotFound'])
    def get(self, profession_id):
        """Get profession details by ID"""
        profession = facade.get_profession(profession_id)
        
        if not profession:
            api.abort(404, "Profession not found")

        owner_data = place.owner.to_dict()
        del owner_data['is_admin']
        
        total_rating = sum(review.rating for review in profession.reviews)
        total_reviews = len(profession.reviews)
        reviews_data = [review.to_dict() for review in profession.reviews]
        for review in reviews_data:
            review_user = facade.get_user(review.get("user_id"))
            review["user_firstName"] = review_user.first_name
            del review['place_id'] 
        profession_dict = profession.to_dict()
        profession_dict['owner'] = owner_data
        profession_dict['reviews'] = reviews_data

        return profession_dict, 200

    @api.expect(models['ProfessionUpdate'])
    @api.response(200, 'Profession updated successfully', models['Updated'])
    @api.response(404, 'Profession not found', models['NotFound'])
    @api.response(400, 'Invalid input data', models['InvalidInput'])
    @api.response(403, 'Unauthorized action', models['UnauthorizedAction'])
    @jwt_required()
    @api.doc(security='token')
    def put(self, place_id):
        """Update a profession's information"""
        current_user = get_jwt_identity().get('id')
        user = facade.get_user(current_user)
        profession = facade.get_profession(profession_id)
        
        if not profession:
            api.abort(404, "Profession not found")

        if not user or place.owner_id != user.id:
            api.abort(403,'Unauthorized action')

        profession_data = api.payload
        
        valid_inputs = ["title", "description", "price"]
        for input in place_data:
            if input not in valid_inputs:
                api.abort(400, f"Invalid input data: {input}")

        try:
            facade.update_profession(profession_id, profession_data)
        except (ValueError, TypeError) as e:
            api.abort(400, str(e))
        
        return {"message": "Profession updated successfully"}, 200

@api.route('/<profession_id>/reviews')
class ProfessionReviewList(Resource):
    @api.response(200, 'List of reviews for the profession retrieved successfully', models['ReviewsProfessionList'])
    @api.response(404, 'Profession not found', models['NotFound'])
    def get(self, profession_id):
        """Get all reviews for a specific profession"""
        profession = facade.get_profession(profession_id)

        if not profession:
            api.abort(404, 'Profession not found')
        
        reviews = facade.get_reviews_by_profession(place.id)
        profession_reviews_list = [
            {key: value for key, value in review.to_dict().items() if key not in ["user_id", "profession_id"]}
            for review in reviews
        ]

        return profession_reviews_list, 200
