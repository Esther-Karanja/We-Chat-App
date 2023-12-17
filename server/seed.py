from app import app
from models import Article, Author, Author_Article, db

with app.app_context():

    Article.query.delete()
    Author.query.delete()
    Author_Article.query.delete()

    authors =[]

    authors.append(Author(name ='Martin'))
    authors.append(Author(name ='Lucy'))
    authors.append(Author(name ='Mitchelle'))
    authors.append(Author(name ='Esther'))

    db.session.add_all(authors)

    articles =[]

    articles.append(Article(title= 'Coding is fun!', body='Indeed coding is fun, its all about practice to make perfect.'))
    articles.append(Article(title= 'Phase 4 group project!', body='We are now working on phase 4 group project, yay!.'))
    articles.append(Article(title= 'Happy Coding!', body='We are using react front end and flask backend to build our app!'))
    
    db.session.add_all(articles)

    author_articles =[]

    author_articles.append(Author_Article(review='excellent!', author= authors[0], article=articles[1]))
    author_articles.append(Author_Article(review='good!', author= authors[2], article=articles[2]))
    author_articles.append(Author_Article(review='nice!', author= authors[3], article=articles[0]))
    author_articles.append(Author_Article(review='brilliant!', author= authors[1], article=articles[1]))
    author_articles.append(Author_Article(review='great!', author= authors[2], article=articles[2]))
    author_articles.append(Author_Article(review='very nice!', author= authors[0], article=articles[0]))
    author_articles.append(Author_Article(review='Fantastic!', author= authors[3], article=articles[1]))
    author_articles.append(Author_Article(review='educative!', author= authors[1], article=articles[2]))
    author_articles.append(Author_Article(review='okay!', author= authors[0], article=articles[1]))

    db.session.add_all(author_articles)
    db.session.commit()


