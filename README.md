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