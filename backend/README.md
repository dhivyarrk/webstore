connect to postgresql as postgres default user

``` 
sudo -u postgres psql
```

create user with password

```
create user webstore_user with encrypted password '12345';
```

Create database

'''
create database webstore_database;
'''

Provide enough privileges for the user to access the database

'''
webstore_database=> set role postgres;
SET
webstore_database=# grant all privileges on schema public to webstore_user;
GRANT

grant all privileges on database webstore_database to webstore_user;
grant all privileges on schema public to webstore_user;
'''

Create migrations:

```
git clone <repository>
cd multipledb
flask --app=flaskbackendmultipledb db init
flask --app=flaskbackendmultipledb db migrate
flask --app=flaskbackendmultipledb db upgrade
```

Run app

```
flask --app=backend run
```

```
http://127.0.0.1:5000
'''
