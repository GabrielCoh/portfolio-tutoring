#!/usr/bin/python3

from app import db
import uuid
from .base import BaseModel
from sqlalchemy.orm import validates


class Review(BaseModel):
    __tablename__ = 'reviews'

    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    profession_id = db.Column(db.Integer, db.ForeignKey('professions.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
            
    def to_dict(self):
        return {
            "id": self.id,
            "rating": self.rating,
            "text": self.text,
            "profession_id": self.profession_id,
            "user_id": self.user_id
        }

    @validates('text')
    def validate_text(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Text is not valid")
        if not value:
            raise TypeError("Text is required")
        return value

    @validates('rating')
    def validate_rating(self, key, value):
        if not value:
            raise TypeError("Rating is required")
        if not isinstance(value, int):
            raise TypeError("Rating is not valid")
        if value < 1 or value > 5:
            raise ValueError("Rating must be between 1 and 5")
        return value
