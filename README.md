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

# env.py of alembic
Open the alembic/env.py and add below line of code 

```
*******************

from database.dbconnection import Base # by atul

from database.model import * # by atul
target_metadata = Base.metadata

***********************

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

14. create a index.html file in /var/www/fprofile directory for test

```
(venv) ubuntu@********122:/var/www/fprofile$ touch index.html
```

15. change the /etc/nginx/sites-available/default file permission

```
(venv) ubuntu@********122:/etc/nginx/sites-available$ sudo chmod ugo+rwx default

```
16. change root in default file 

```
server {
************
	root /var/www/fprofile;

************
}
```

17. restart nginx

```
(venv) ubuntu@********122:/etc/nginx/sites-available$ sudo systemctl restart nginx

```

18. Before uploading create requirements.txt file again in your local machine

```
(env) atul@atul-Lenovo-G570:~/fprofile1$ pip3 install -r requirements.txt

```

19. Upload all dirctory and files in fprofile
  - Note1: do not upload .git and virtual environment dirctory like env


20. install requirments.txt

```
 (env):/var/www/fprofile$ pip3 install -r requirments.txt

```

21. Test the nginx configuration
```
:etc/nginx/sites-available$ sudo nginx -t
```
You will see <b>Syntax is ok </b> if all cofiguration correct.

22. install net-tools package to check IP address and port

```
apt install net-tools

```

23. edit the /etc/nginx/sites-available/default

   - server_name: your public IP address or domain name

```

server {

************
	server_name 107.22.13.121;

	location / {
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
		proxy_pass http://0.0.0.0:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;

	}
********************

}


```
  - Add rule in ec2 intance to open 8080 port from security group


24. We can run uvicorn command using three way nohup, tmux and screen. You can use only one way to run uvicorn command. Here we are describing nohup and tmux.
   - Note: tmux latest and it has better functioalities from screen.
   - Note: Deploy your project and run uvicorn using tmux. because it is better than nohup

25. Run uvicorn using nohup command

url for help: https://www.geeksforgeeks.org/nohup-command-in-linux-with-examples/

- run the nohup uvicorn main:app --host 0.0.0.0 and --port 8080 --reload > uvicorn.log 2>&1 & because we have set the proxy_pass in /etc/nginx/sites-available/default file
- note: If you run uvicorn command with --reload then you can upload changes and your change will be reflect. Some time you have need to fix the bug

```
 # run with --reload option
 (env):/var/www/fprofile$ nohup uvicorn main:app --host 0.0.0.0 --port 8080 --reload > uvicorn.log 2>&1 &

 # Or run without --reload option
 (env):/var/www/fprofile$ nohup uvicorn main:app --host 0.0.0.0 --port 8080 > uvicorn.log 2>&1 &


```
 - run the nohup uvicorn main:app --host 0.0.0.0 and --port 8080 --reload > uvicorn.log 2>&1 & because we have set the proxy_pass in /etc/nginx/sites-available/default file
 - note: If you run uvicorn command without --reload then you can upload changes but your chage will not be reflect. Your project stable and you have not need to change then run uvicorn without --reload option

 - Now you can close your ssh or putty and check your public IP address your fastapi project is running

 - check running process

 ```
 sudo netstat -plten |grep ':8080'

 ```
 - If you run your uvicorn command without --reload and you want to upload some chage and you want to reflect your change then you can kill the process
 - After killing process your project will give forbiden error

 command: kill -9 [process ID (PID)]

 ```
 kill -9 16085 

 ```

26. Run uvicorn using tmux
   - Install tmux in ec2 instance if not installed
   - create a session in tmux. here 

   $ tmux new -s [session_name]

   ```
    $ tmux new -s tmux_fprofile
    
   ```

   - You will go in a tmux screen. Here you can run any command.
   - new activate the vertual environmennt

   ```
    ubuntu@***:/var/www/fprofile$ source env/bin/activate

   ```
   - Now run uvicorn command in this tmux window
     command: uvicorn main:app --host 0.0.0.0 --port 8080 --reload > uvicorn.log 2>&1 &
  
   ```
    #run uvicorn with --reload option

   (env):/var/www/fprofile$ uvicorn main:app --host 0.0.0.0 --port 8080 --reload > uvicorn.log 2>&1 &
    
    #run uvicorn without --relaod option

   (env):/var/www/fprofile$ uvicorn main:app --host 0.0.0.0 --port 8080 > uvicorn.log 2>&1 &

   ```
   - Now check browser using public IP address
   - Run the tmux ls command to show session_list 
   - note: If you run uvicorn command with --reload then you can upload changes and your change will be reflect. Some time you have need to fix the bug
   - note: If you run uvicorn command without --reload then you can upload changes but your chage will not be reflect. Your project stable and you have not need to change then run uvicorn without --reload option

     ```
       $ tmux ls

     ```

   - Detaching from a tmux session
     - type Ctrl-b  then press d
     - now you will come in linux terminal
   - Attach again from session
     - run the below command
       command: $ tmux a -t [session_name]

       ```
        $ tmux a -t tmux_fprofile

       ```
 - You can type exit command to exit from tmux window and you come in ubunut terminal
      
      ```
      $ exit

      ```
      - But now you can see your session is not available so you detach instead of exit command 
       
      ```
      $ tmux ls

      ``` 
      - But if you check netstate then you application and port is running

      ```
      $ sudo netstat -plten

      ```
 - Now you can close your ssh or putty and check your public IP address your fastapi project is running

27. tmux is better than nohup and screen so deploy fastapi project with tmux.
   - Fastapi source code you run using nginx server

28. After some time letter like 3 month or 6 month and you not remember that you run uvicorn with tmux or nohup then and you want to stop the running of project then kill the process usig kill command. And you run again uvicorn command to run your applicatio.

29. set the alembic.ini file

sqlalchemy.url = postgresql://postgres:[password]@[endpoint]:5432/fprofile_db

```
sqlalchemy.url = postgresql://postgres:123456789@testpostresql.ctk6csmmwzzi.us-east-1.rds.amazonaws.com:5432/fprofile_db

```

30. set the .env file for database connection

