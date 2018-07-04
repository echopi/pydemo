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
