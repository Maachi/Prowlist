#Prowlist

## Installation

### Virtual enviroment
1. Install virtual enviroment requirements  
2. Install virtual enviroment wrapper to facilitate the configuration `pip install virtualenvwrapper`
3. Next, create a folder that will contain all your virtual environments if not exists `mkdir ~/.virtualenvs`
4. Open your .bashrc `vi ~/.bashrc` file and add: 
	export WORKON_HOME=~/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh
5. Activate these changes by typing `source ~/.bashrc`
6. Create virtual `enviroment prowlist`
7. Initialize enviroment `workon prowlist`

The following dependencies are needed to run this environment:

1. Install all dependencies `pip install -r requirements.txt`

Note: Do not forget to run `pip freeze > requirements.txt` after adding any library or component

## Installation Dev-Enviroment Instructions for MacOSX 

1. There is a remote database installed, updated with all migrations ready for you to develop, if the responses do not facilitate the dev work, you should install MySQL and properly set up your development environment.

## Run the project

The application uses Django 1.8 run the following command line after changing a model
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

## Application

Prowlist has the following services integrated:

### Image Server 

If you want to access to the image server just write the following path `/services/image/WxH/Path`

