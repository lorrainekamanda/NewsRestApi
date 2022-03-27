# Introduction

This is a  News Api Django rest Framework project that focuses on the CRUD functionalities of Restful Api..

## Resources
The following are the resources used by the project:

  - [Docker](https://www.docker.com/) - for virtual development environment and easy deployment
  - [Postman](https://startbootstrap.com/theme/sb-admin-2) -For assement of the Apis
  - [Heroku](https://newsboardapi.herokuapp.com/) - for very easy production deployment.

## Prerequisites
As a prerequisite please make sure you have the following tools already installed on your machine:
1. [Git](https://git-scm.com/)
2. [Docker](https://docs.docker.com/get-docker/)
3. [Docker Compose](https://docs.docker.com/compose/install/)
4. [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) - Note: you'll need to create a Heroku account and there may be a cost associated with the servers you use.
5. [VirtualEnv](https://docs.python.org/3/tutorial/venv.html)
```sh
$ python3 -m virtualenv DjangoInMinutesStarterProject

```

## Installing the app using Django!
1. Clone this repo
```sh
$ git clone git@github.com:NoahFinberg/djangostarterproject.git
```

[Github](https://github.com/) - You want to set up a new Github repo for this code so you can make changes for your own project. (also needed for deploying to Heroku)
```sh
git remote set-url origin <remote> # remote is git url to your repo.
git push origin main
```

2. Build the Docker Container
```sh
$ cd djangostarterproject
$ docker-compose up --build
```
You should see all the resources including the web server startup in your terminal. Now, open up another terminal window in the same directory.

3. Populate Postgres DB
```sh
$ cd djangostarterproject
$ docker-compose exec web python manage.py migrate
```
Now refresh `localhost:8000`. That should be enough for you to run the starter project locally. Seriously, that's it! One thing to note is if you change some settings in the Dockerfile or docker-compose.yml files, you'll need to rebuild the docker container.

If you'd like to deploy your project to Heroku, that's also pretty simple now. Just use the following commands:
```sh
# generates a new Heroku app
heroku create 
# creates new postgres db
heroku addons:create heroku-postgresql:hobby-dev 

# sets the SECRET KEY in production. You'll need to generate one. You can use - [https://djecrety.ir/](https://djecrety.ir/) or [https://miniwebtool.com/django-secret-key-generator/](https://miniwebtool.com/django-secret-key-generator/) if you'd like.
heroku config:set SECRET_KEY='replace me with a generated secret key'

# deploy to Heroku
git push heroku main
heroku open
```
Congrats! You now have a pretty great starting point for your Django project.



## Helpful Docker + Django Commands ##
```sh
# rebuild docker container
docker build .
# start docker container
docker-compose up
# shutdown docker-container
docker-compose down


# generate db migrations
docker-compose exec web python manage.py makemigrations
# run db migrations
docker-compose exec web python manage.py migrate
# start new app
docker-compose exec web python manage.py startapp <app name>
# shell into docker container
docker-compose exec web python manage.py shell

```

## License
I've made this starter application freely available under an MIT license. 



