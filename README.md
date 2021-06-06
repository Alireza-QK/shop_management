# shop management

## shop management with django

<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/Alireza-QK/shop_management/master/shop_management.png" width="900"></a></p>


## used:
- python3.8 | DJANGO framework - version 3.2
- MariaDB 
- Bootstrap 4 & JQuery


## Create Database in MariaDB:
- go to ``` sudo mysql -u root -p ```
- use this for create database ``` CREATE DATABASE 'yourDB'; ```
- Create New MariaDB User ``` CREATE USER 'user1'@localhost IDENTIFIED BY 'password1'; ```
- Grant Privileges to MariaDB User ``` GRANT ALL PRIVILEGES ON *.* TO 'user1'@localhost IDENTIFIED BY 'password1'; ```
- To grant privileges only for yourDB ``` GRANT ALL PRIVILEGES ON 'yourDB'.* TO 'user1'@localhost; ```
- and use ``` FLUSH PRIVILEGES; ```

## Config seeting.py in your project:
- open `` settings.py `` on your folder project
- change config database


## to use this app:
- install python3, pip3, virtualenv
- clone the project 
- create a virtualenv named venv using ``` virtualenv -p python3 venv```
- Connect to virtualenv using ``` source venv/bin/activate ```
- from the project folder, install packages using ``` pip install -r requirements.txt ```
- finally ```$ python manage.py runserver```
