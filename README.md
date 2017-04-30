Bookstore Django application:

A simple bookstore application where users can add/remove books and make reviews about them

Installation :

1-Make sure you have MySQL server up and running
2-setup a database using this command from the terminal

echo "create database django_bookstore" | mysql -u username -p

3-If the last command failed, you can create the database manually and name it "django_bookstore"

4-Clone Repo into your favourite directory

5-Enter the application's directory and make the migrations to set the database scheme

python3 manage.py makemigrations
python3 manage.py migrate

5-Run the application using the following command

python3 manage.py runserver

6-You can find the application running on http://localhost:8000

7-Register an account to start using the app 
