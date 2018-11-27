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
# env FLASK_APP=app.py flask run
./start.sh
```

## test

```sh
curl 'http://127.0.0.1:5000/api/json/test' -H 'accept: application/json' -H 'content-type: application/json' --data-binary '{"method":"startTask","network":"3g","clearCache":true,"login":false,"user":{"name":"nobody","job":"cool"},"simulator":true,"configPath":"config/perf-config.js","url":"https://m.douban.com","extraParams":{"reportId":1,"runtime":"lighthouse"}}' --compressed
```

## issue

```sh
sudo chown -R $USER /Library/Python/2.7
```

## references

* flask docs: http://flask.pocoo.org/docs/1.0/
