from flask import Flask, jsonify, request, make_response
from  flask_migrate import Migrate
from flask_cors import CORS

from models import db, Article

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


migrate = Migrate(app, db)

db.init_app(app)

#routes, GET, POST,PATCH,DELETE

@app.route('/')
def home():
    return 'welcome to Articles app!'

#gets all articles
@app.route('/articles', methods=['GET'])
def get_articles(): 
    articles =[]

    for article in Article.query.all():
        article ={
            "id": article.id,
            "title": article.title,
            "body": article.body,
            "topic": article.topic,
            "description": article.description,
            "created_at": article.created_at,
            "updated_at": article.updated_at
        }
        articles.append(article)
        response = make_response(jsonify(articles),200)
    return response 

#get one article by id
@app.route('/articles/<int:id>', methods =['GET'])
def get_article_byID(id):
    article = Article.query.filter_by(id=id).first()

    if article == None:
        response = make_response(
                jsonify({
                    "error": "article not found!"
                    }),
                404
        )
        return response   
    else:

        article_dict =article.to_dict()

        response = make_response(
            jsonify(article_dict),
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response

#create a new article
@app.route('/add_article', methods=['POST'])
def add_article():
    new_article = Article(
       title= request.form.get('title'),
       body =request.form.get('body')
    )

    db.session.add(new_article)
    db.session.commit()

    response = make_response(
            jsonify(new_article.to_dict()),
            201
        )
    return response

#patch an article
@app.route('/articles/<int:id>', methods =['PATCH'])
def update_article(id):

    article = Article.query.filter_by(id=id).first()

    for attr in request.form:
        setattr(article, attr, request.form.get(attr))


    db.session.add(article)
    db.session.commit()

    article_dict = article.to_dict()

    response = make_response(
        jsonify(article_dict),
        200
    )

    return response

#delete an article
@app.route('/articles/<int:id>', methods=['DELETE'])
def delete_article(id):

    article = Article.query.filter_by(id=id).first()

    db.session.delete(article)
    db.session.commit()

    response = make_response(
        jsonify({
            'message': 'Article deleted successfully!'
        }),
        200
    )

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)