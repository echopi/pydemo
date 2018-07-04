# python demo

## init virtualenv

```sh
pip install --upgrade pip
pip install virtualenv

virtualenv ENV
```

## active & deactivate

```sh
source ENV/bin/activate

deactivate
```

## freeze

```sh
pip freeze > requirements.txt
pip install -r requirements.txt
```

## start app

```sh
env FLASK_APP=app.py flask run
```

## references

* flask docs: http://flask.pocoo.org/docs/1.0/
