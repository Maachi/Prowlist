#Prowlist

## Installation

The following dependencies are needed to run this environment:

1. XMLToDict library `pip install xmltodict`
2. Tastypie library `pip install django-tastypie`
3. boto: Required for storages amazon interfaces sudo `pip install boto`
4. Storages: [http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html] `pip install django-storages`
5. Django ses `pip install django-ses`

## Installation Dev-Enviroment Instructions for MacOSX 

1. Download latest Django, follow instructions here: [https://www.djangoproject.com/download/]
2. Download the latest MySQL. [http://dev.mysql.com/downloads/]
3. Download the latest MySQL-python package [http://sourceforge.net/projects/mysql-python/files/mysql-python/]
4. Unzip the MySQL-python-1.2.3.tar.gz
5. Edit site.cfg on your favorite text editor and change the mysql path as below: 

`mysql_config = /usr/local/mysql/bin/mysql_config`

6. You are now ready to build and install MySQL-python:
7. Now build the library (Run this in your terminal). `python setup.py build`
8. Now install it. `sudo python setup.py install`
9. Edit your ~/.bash_profile, add the following line:

`export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/`

## Run the project

The application uses Django 1.7 run the following command line after changing a model
`./manage.py makemigrations`
Running the application
`./manage.py migrate`

## Migrations

1. Database synchronization `./manage.py syncdb`
2. Running the application `./manage.py runserver`
3. If is a new Application and you want to add migration run the following command `./manage.py makemigrations` new_app and then `./manage.py migrate`
4. If you want to save data relevant for the development or deployment run `./manage.py dumpdata --indent=4 > resources/data/NAME_OF_FILE.json`
5. If you want to load data to your database run `./manage.py load initial`

## Stage build

1. Make sure you have pxshh installed, if not `pip install pexpect` You need a Unix based os to run the installer
2. You need to have the Private key to connect.
3. Run the following command `./manage.py publish stage`
4. The process will take a few minutes.

