cd authorization
docker run --rm -v $PWD:/app/io macterra/metatron-type
cd ..
docker run --rm -v $PWD:/app/io macterra/metatron-asset 
ipfs add -r .

