docker run --rm -d -p 6379:6379 --name redis  -v $PWD/data/redis:/data redis

sleep 2

. ./metatron.env

export FLASK_APP=vault
export FLASK_ENV=development
export SECRET_KEY='scully:sw33tp0tat0'

flask run --port=5000