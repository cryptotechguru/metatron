docker run --rm -d -p 6379:6379 --name redis  -v $PWD/data/redis:/data redis

sleep 2

. ./metatron.env

export FLASK_APP=vault
export FLASK_ENV=development

flask run --port=5000