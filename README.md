Welcome to the We-Chat App.

This is a full stack web app that allows users to share messages

setup instructions:
create server, client directories

# backend
cd into server, activate virtual env(pipenv install, pipenv shell)
to install packackages used to create this app, run  pip install -r requirements.txt in your terminal
(____!remember to create a requirements.txt once done!! pip freeze > requirements.txt )
to run the backend - use flask run

models.py - created 3 models Author, Articles, Author_Articles

An Author has many Articles through Author_Articles
An Article has many Authors through Author_Artticles
A Author_Articles belongs to an Author and belongs to an Article

migration handled by running, flask db init, flask db migrate, flask db upgrade.
create a seed.py file for seed data then run python seed.py to add seed data to the models

in app.py, create routes
install Cors to allow communication between Flask backend and React frontend

# frontend
cd into client, create a react app( npx create-react-app we-chat) to install react packages
and create react project structure
can now run frontend by cd we-chat , then run npm start or open http://localhost:3000 in your browser

# Fetching Data 
on app.js , use hooks(useState and useEffect to fetch our articles data from the server)  
create an ArticleList file in components to contain our Articles
install bootsrap using npm install bootstrap command


