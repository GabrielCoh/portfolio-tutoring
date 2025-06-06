#!/usr/bin/python3

from app import db
import uuid
from .base import BaseModel
from .associations import place_amenity
from sqlalchemy.orm import validates, relationship


class Place(BaseModel):
    __tablename__ = 'places'
    
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner = relationship("User", back_populates="profession")
    reviews = relationship('Review', backref='users', lazy=True)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def remove_review(self, review):
        """Remove a review to the place"""
        self.reviews.remove(review)
        
    def update(self, data):
        if "title" in data:
            self.title = data["title"]
        if "description" in data:
            self.description = data["description"]
        if "price" in data:
            self.price = data["price"]
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "created_at": self.created_at.strftime('%d/%m/%Y')
        }

    @validates('title')
    def validate_title(self, key, value):
        if not value:
            raise TypeError("Title is required")
        if not isinstance(value, str):
            raise TypeError("Title value is not valid")
        if len(value) > 100:
            raise ValueError("Title is too long")
        return value

    @validates('description')
    def validate_description(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Description value is not valid")
        return value

    @validates('price')
    def validate_price(self, key, value):
        if not value:
            raise TypeError("Price is required")
        if not isinstance(value, (float, int)):
            raise TypeError("Price value is not valid")
        if value < 0:
            raise ValueError("Price must be a positive number")
        return value
