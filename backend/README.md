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
grant all privileges on database webstore_database to webstore_user;
grant all privileges on schema public to webstore_user;
'''

Run app

```
flask --app=backend run
```
