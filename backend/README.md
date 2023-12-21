# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###


* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact

### Summary of set up

This is setup for Windows

* Clone the repository 
`git clone `

* Setup Virtual environment
`virtualenv env`

* Activate Virtual Environment
`env\scripts\activate`

* Move to  folder
`cd `

* Install the requirements.txt
`pip install -r requirements.txt`

### Configuration

* Install MySQL connectors 
`pip install pymysql`
`pip install mysqlclient`

### Database configuration

* Install MariaDB locally

* Login using root user privellages

* Create new database
`CREATE DATABASE `

* Update settings_local.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost', 
        'PORT': '3306',   
    }
}

* Migrate the DB

`python manage.py makemigrations`

`python manage.py migrate`


### Test the server

`python manage.py runserver`
=======
* Other community or team contact