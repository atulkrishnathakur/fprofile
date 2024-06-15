# fprofile
fastapi project

# install fastapi
```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 install "fastapi[all]"

```

# generate requirements.txt
```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 freeze > requirements.txt

``` 

# run the server
The command uvicorn main:app refers to:

1. main: the file main.py (the Python "module").
2. app: the object created inside of main.py with the line app = FastAPI().
3. --reload: make the server restart after code changes. Only use for development.

```
uvicorn main:app --reload

```

# install sqlalchemy
```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 install sqlalchemy

```

# install psycopg2-binary

```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 install psycopg2-binary

```

# install alembic
```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 install alembic

```

Below command will create an alembic directory with necessary configuration files.

```
(env) atul@atul-Lenovo-G570:~/fprofile$ alembic init alembic

```

# alembic.ini
Open the alembic.ini file in the alembic directory and make the following changes:

```
sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/fprofile_db

```

# Auto Migration
If you want alembic handles migrations follow this method: In the alembic folder edit env.py and find target_metadata line and edit like the following

import the "from main import Base" in alembic/env.py file
and set the "target_metadata = Base.metadata" in alembic/env.py file

Reference url https://fastapi.blog/blog/posts/2023-07-20-fastapi-sqlalchemy-migrations-guide 

# Generating a Migration

```
(env) atul@atul-Lenovo-G570:~/fprofile$ alembic revision --autogenerate -m "Initial migration"
```

# Applying the Migration

```
(env) atul@atul-Lenovo-G570:~/fprofile$ alembic upgrade head

```

# Hashing
create password hashing
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 install "passlib[bcrypt]"

```


# JWT Authentication
1. install python-jose
```
(env) atul@atul-Lenovo-G570:~/fprofile$ pip3 install python-jose
```

## generate SECRET_KEY of JWT
1. run the below command to generate SECRET_KEY of JWT like  a9e53f2c3db459d04f147f11a056a705f87fbbba6204a42efb9a37b4aed9cf48

```
(env) atul@atul-Lenovo-G570:~/fprofile$ openssl rand -hex 32
```


# How to install nginx in local machine
1. run the below command to install nginx
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04

```
sudo apt update
sudo apt install nginx

```
# adjusting the firewall (without need not enable the ufw)

1. list after running ufw command 

```
$ sudo ufw app list


# output is like blow
Available applications:
  Apache
  Apache Full
  Apache Secure
  CUPS
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
```

. enable the ufw status

```
:~$ sudo ufw enable
```

2. check ufw status

```
:~$ sudo ufw status
```

3. run the below command to allow

```
:~$ sudo ufw allow 'Nginx Full'

#output like below
Rules updated
Rules updated (v6)
```

4. if apache2 already installed then stop the apache2
```
 sudo systemctl stop apache2
```
5. again start nginx
```
atul@atul-Lenovo-G570:~$ sudo systemctl start nginx

```
6. now check nginx status

```
atul@atul-Lenovo-G570:~$ systemctl status nginx

``` 

7. check the nginx

  - run public IP address or domain in browser like http://54.**.212.250/


8. Important note: If you enable the ufw in aws ec2 instance then you can not access the ec2 instance using SSH. You cannot access from putty. You cannot connect ec2 instance after clicking on connect button in aws ec2 instance.

# Deployment on AWS
1. create ec2 instance if not created in aws 
2. Install nginx server if not installed 
3. Do not enable the ufw command. Otherwise you cannot connect ec2 instance by ssh. You cannot connect from putty. You cannot connect after clicking connect command.

3. create in fprofile directory in /var/www in ec2 instance
```
sudo mkdir /var/www/fprofile
```
4. change permission  

```
sudo chmod ugo+rwx fprofile
```

5. check python version
```
:~$ python3 -V
```
6. Install python version according to you. In this application we are using python3.10 version so install python version according to your requirement
   - Add the PPA

   ```
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update

   ```

   - Intall python3.10

   ```
   sudo apt install python3.10
   ```
   - Check version

   ```
    python3.10 -V
    # or
    python3.10 --version

   ```

7. install the python virtual environment
```
:~$ sudo apt install python3.10-venv
```

8. create the virtual environment
```
:/var/www/fprofile$ python3.10 -m venv env
```
note env is the virtual directory name


9. check activate and deactivate of virtual directory
- activate
```
:/var/www/fprofile$ source env/bin/activate
```
- deactivate
```
:/var/www/fprofile$ source env/bin/deactivate
```

10. activate the virtual environment
```
:/var/www/fprofile$ source env/bin/activate

```

11. check again python version

```
(venv) ubuntu@********122:/var/www/fprofile$ python -V

# Or

(venv) ubuntu@********122:/var/www/fprofile$ python3 -V

# in output you can see Python3.10.14
```

12. check pip version

```
(venv) ubuntu@********122:/var/www/fprofile$ pip -V

# Or

(venv) ubuntu@********122:/var/www/fprofile$ pip3 -V

# you can see pip 23.0.1 using both above command

```
13. change pip version if you have requirements

```
(venv) ubuntu@********122:/var/www/fprofile$ python3.10 -m pip install pip=22.0.1

```

12. create a index.html file in /var/www/fprofile directory for test

```
(venv) ubuntu@********122:/var/www/fprofile$ touch index.html
```

13. change the /etc/nginx/sites-available/default file permission

```
(venv) ubuntu@********122:/etc/nginx/sites-available$ sudo chmod ugo+rwx default

```
14. change root in default file 

```
server {
************
	root /var/www/fprofile;

************
}
```

15. restart nginx

```
(venv) ubuntu@********122:/etc/nginx/sites-available$ sudo systemctl restart nginx

```

16. Before uploading create requirements.txt file again in your local machine

```
(env) atul@atul-Lenovo-G570:~/fprofile1$ pip3 install -r requirements.txt

```

12. Upload all dirctory and files in fprofile
  - Note1: do not upload .git and virtual environment dirctory like env


14. install requirments.txt

```
 (env):/var/www/fprofile$ pip3 install -r requirments.txt

```

15. Test the nginx configuration
```
:etc/nginx/sites-available$ sudo nginx -t
```
You will see <b>Syntax is ok </b> if all cofiguration correct.

