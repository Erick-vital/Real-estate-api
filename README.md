# Real-estate-api
A simple real estate api with django rest framework 

## Installation


After you cloned the repository, you want to create a virtual environment, 
so you have a clean python installation. You can do this by running the command
```
python -m venv venv
```
After this, it is necessary to activate the virtual environment, ypu can run the following command, you can get more information 
about this [Here](https://docs.python.org/3/tutorial/venv.html)

Now that the virtual environment is running you can install all the required dependencies by running
```
pip install -r requirements.txt
```

## Use
First, we have to start up Django's development server
```
python manage.py runserver
```
Now you can see all the real estate objects using the url, you can also add new objects in this url
```
http://127.0.0.1:8000/inmuebles
```
To see an specific object
```
http://127.0.0.1:8000/inmuebles/1
```
To update an object
```
http://127.0.0.1:8000/inmuebles-update/1
```
To delete an object
```
http://127.0.0.1:8000/inmuebles-delete/1
```

You can change the number **1** for and specific id
