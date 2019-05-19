1. Clone the source code onto your local repository
```
Git clone https://github.com/suot/sportsStore.Git
```
2. Open it with PyCharm, "Tools->Run manage.py Task...", "Run"
3. Open a browser and add/edit/delete data on the admin page "http://127.0.0.1:8000/admin"
4. Edit the "models.py" file to change the sqlite3 db models and type in the manage.py console:
```
makemigrations store
```
```
sqlmigrations store 001 (substitute 001 with the latest file in the migrations dir)
``` 
```
migrate
```
