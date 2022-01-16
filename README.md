# metatron
#### Secure version control for metadata

You can [clone or fork this repository](https://github.com/cryptotechguru/metatron) to get started. 

See the [docs](docs/README.md) for a detailed explination about Metatron.

## Getting started

Metatron relies on IPFS to store metadata.  You will need to have IPFS and IPFS-Shell installed. 
You can get more info about installing IPFS and IPFS-Shell [here](https://docs.ipfs.io/install/).

One IPFS is installed, you can start the IPFS server up by running the following command:


```
ipfs daemon
```

You will also need to have Docker installed.  You can get more info about installing Docker [here](https://docs.docker.com/install/).  Once it is istalled, you can:


Start Metatron by running the following command:

```
sh run.sh
```

#### ipfshttpclinet
MetaTron uses the [ipfshttpclient](https://github.com/ipfs-shipyard/py-ipfs-http-client/tree/09cae7672a39ca3ff991684c1b31cfe7875174c3) to interact with IPFS.  Right now you will need to install version 0.7.0 of the library. 



Navigate to http://localhost:5000


Optionally you run a scanner, e.g.:
```
sh scanTESS.sh
```
