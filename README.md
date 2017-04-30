Bookstore Django application:

A simple bookstore application where users can add/remove books and make reviews about them

Installation :

1-Make sure you have MySQL server up and running

2-setup a database using this command from the terminal

echo "create database django_bookstore" | mysql -u username -p

3-If the last command failed, you can create the database manually and name it "django_bookstore"

4-Clone Repo into your favourite directory

5-Browse to the application's directory and make the migrations to set the database scheme

python3 manage.py makemigrations

python3 manage.py migrate

6- create an admin account using the command

python manage.py createsuperuser


7-Run the application using the following command

python3 manage.py runserver

8-You can find the application running on http://localhost:8000

9-Register an account to start using the app

Contributors :

Hassan Mohammed ( hassanmamin994@gmail.com )
