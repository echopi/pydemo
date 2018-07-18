#/bin/bash

count=`ps aux | grep redis | grep 6379 | wc -l`

[ $count == '0' ] && [ -x "$(command -v redis-server)" ] && redis-server &

# env FLASK_APP=app.py flask run
