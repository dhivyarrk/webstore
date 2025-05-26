**Web application link:** https://booboofashions.netlify.app/ 

**Source code**

Backend code: https://github.com/dhivyarrk/webstore <br>
Frontend code: https://github.com/dhivyarrk/fullstackfrontendapp <br>
Frontend deployment: https://booboofashions.netlify.app/ <br>
Backend deployment: https://booboofashionsgunic.onrender.com (cannot be accessed by internet) 

**Project architecture:**

Frontend: Angular – hosted on netlify <br>
Backend: flask – hosted on render <br>
Database: postgres – hosted on render <br>

Test results: https://github.com/dhivyarrk/webstore/issues 

# Documentation: 

*Service name:* Boo Boo fashions  

*Description of the service:* Online web store where customer's can purchase kid’s clothes, kid’s shoes, women’s clothes and women’s accessories. 

*Detailed description:*
Kid’s clothes, kid’s shoes, women’s clothes and women’s accessories are sold in this website. Customer's can login through third party sso (single-sign-on) or create account, browse inventory,  add items to their cart, checkout, pay through card or cash on delivery. 

## Installation instructions:  

### To run locally (Tested in ubuntu 24.04 lts) 

*1. Install postgres:*

 1.1 Install postgresql service 
```
sudo apt install postgresql 
```
1.2 start postgresql service 
```
sudo service postgresql start
sudo service postgresql status  
```
1.3 connect to postgresql as postgres default user: 
```
sudo -u postgres psql 
```
1.4 create user with password 
```
create user webstore_user with encrypted password '12345'; 
```
1.5 Create database 
```
create database webstore_database; 
```
1.6 Provide enough privileges for the user to access the database 
```
webstore_database=> set role postgres;  
webstore_database=# grant all privileges on schema public to webstore_user;  
grant all privileges on database webstore_database to webstore_user;  
grant all privileges on schema public to webstore_user;  
```

*2. For backend server:*

 2.1 Clone the repository: 
```
git clone git@github.com:dhivyarrk/webstore.git 
```
2.2 Clean migration folder if already present: 
```
cd webstore 
rm -rf migrations
```
2.3 Initiate db and run migrations for database: 
```
flask --app=backend db init 
flask --app=backend db migrate 
flask --app=backend db upgrade 
```
2.4 change config to use local postgres db:
a. uncomment this line in config.py: 

https://github.com/dhivyarrk/webstore/blob/main/backend/config.py#L4 

b. comment this line: 

https://github.com/dhivyarrk/webstore/blob/main/backend/config.py#L5 

2.5 Run the application: 
```
flask –app=backend run 
```
*3. For frontend server:*

3.1 Clone repository: 
```
git clone git@github.com:dhivyarrk/fullstackfrontendapp.git 
```
3.2 Change env.ts to connect to local backend server: 
```
cd fullstackfrontendapp 
```
a. uncomment local server https://github.com/dhivyarrk/fullstackfrontendapp/blob/main/src/app/env.ts#L1 

d. comment the online deployment server https://github.com/dhivyarrk/fullstackfrontendapp/blob/main/src/app/env.ts#L2 

3.3. run server: 
```
ng serve 
```
(if there are any issues please remove node-modules (rm -rf node-modules) and package-lock.json(rm package-lock.json) and run again) 

*4. For google singe sign on(SSO) to work locally:*  

a. uncomment this line: 

https://github.com/dhivyarrk/webstore/blob/main/backend/__init__.py#L43 

b. comment this line: 

https://github.com/dhivyarrk/webstore/blob/main/backend/__init__.py#L42  

c. change these oauth configs (register app and get oauth credentials from google console): 

https://github.com/dhivyarrk/webstore/blob/main/backend/__init__.py#L48 

d. modify these to use local frontend server 

https://github.com/dhivyarrk/webstore/blob/main/backend/__init__.py#L109 

https://github.com/dhivyarrk/webstore/blob/main/backend/__init__.py#L134 


User manual: 

Important Features: 

As a user: 

1. Signup as an admin or normal customer to use service. 

2. Signin with existing credentials and continue session until logout. 

3. Sign in with the google account. 

4. Can list women’s clothes, women’s accessories, kid’s clothes and kid’s shoes 

5. Add products to cart. 

6. Checkout the cart and choose cash on delivery or card for payment of order. 

7. Send feedback about service through contact form. 

8. Can logout of the service. 

 

As an admin: 

1. Sign in to the service 

2. Signup in the service as an admin 

3. Can list, add, modify women’s clothes 

4. Can list, add, modify women’s accessories 

5. Can list, add, modify kid’s clothes 

6. Can list, add, modify kid’s shoes 

7. Can logout of the service. 

 

Notes/Known issues: 

➢ SSO login with gmail credentials. (please use incognito window if you 

encounter any errors) 

➢ slowness in render (hosting provider) after inactivity. 

 

For Issues that were collected during testing phase (external and internal testing) of the service development: 

 

open issues: https://github.com/dhivyarrk/webstore/issues 

fixed/closed issues: https://github.com/dhivyarrk/webstore/issues?q=is%3Aissue+is%3Aclosed 
