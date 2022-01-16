# metatron
#### Secure version control for metadata

See the [docs](docs/README.md) for a detailed explination about Metatron.

## Getting started

Metatron relies on IPFS to store metadata.  You will need to have IPFS and IPFS-Shell installed. 
You can get more info about installing IPFS and IPFS-Shell [here](https://docs.ipfs.io/install/).

One you have IPFS installed, you can start the IPFS server: up by running the following command:

```
$ ipfs daemon
```

You will also need to have Docker installed.  You can get more info about installing Docker [here](https://docs.docker.com/install/).  Once it is istalled, you can:

Start up redis:
```
sh start-redis.sh
```

Start up the Metatron vault:
```
sh run-vault.sh
```

Navigate to http://localhost:5000



Optionally you run a scanner, e.g.:
```
sh scanTESS.sh
```
