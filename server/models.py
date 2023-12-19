from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint


#Author, Article, Author_Article

db = SQLAlchemy()

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    serialize_rules =('-author_articles.author',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    
    author_articles = db.relationship('Author_Article', backref ='author')

    def __repr__(self):
        return f'author name is {self.name}'


class Article(db.Model, SerializerMixin):
    __tablename__ = 'articles'

    serialize_rules =('-author_articles.author',)

    id = db.Column(db.Integer , primary_key =True)
    title = db.Column(db.String, nullable=False)
    body =db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    author_articles = db.relationship('Author_Article', backref ='article')
    
    def __repr__(self):
        return f'article title is {self.title} and description is {self.body}.'

class Author_Article(db.Model, SerializerMixin):

    __tablename__ ='author_articles'

    serialize_rules =('-author.author_articles', '-article.author_articles',)

    id = db.Column(db.Integer , primary_key =True)
    review = db.Column(db.String(50))
    author_id = db.Column(db.Integer , db.ForeignKey('authors.id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))

    
    def __repr__(self):
        return f'author_article review is {self.review}'
    
#Validations
    @validates('topic')
    def validate_topic(self, key, value):
        if value not in ['Recipies', 'Sports', 'Fashion']:
            raise ValueError("Topics must be one of: 'Parenthood', 'Recipies', 'Sports', 'Fashion'")
        return value

    @validates('description')
    def validate_description(self, key, value):
        if len(value.strip()) < 100:
            raise ValueError("Description must be at least 100 characters long.")
        return value


