# Metatron
#### Secure version control for metadata

You can [clone or fork this repository](https://github.com/cryptotechguru/metatron) to get started. 

See the [docs](docs/README.md) for a detailed explination about Metatron.

## Getting started

#### IPFS

Metatron relies on IPFS to store metadata.  You will need to have IPFS and IPFS-Shell installed. You can get more info about installing IPFS [here](https://docs.ipfs.io/install/).

One IPFS is installed, you can start the IPFS server up by running the following command:


```
ipfs daemon
```

#### Docker

You will also need to have Docker installed.  You can get more info about installing Docker [here](https://docs.docker.com/install/).  


#### ipfshttpclinet
MetaTron uses the [ipfshttpclient](https://github.com/ipfs-shipyard/py-ipfs-http-client/tree/09cae7672a39ca3ff991684c1b31cfe7875174c3) to interact with IPFS.  Right now you will need to install version 0.7.0 of the library for use with Metatron. 



### Start Metatron

The next step is starting Metatron by running the following command:


```
sh run.sh
```

When Metatron is running, you can start using it by navigating to http://localhost:5000


--- 


Optionally you run a scanner, e.g.:
```
sh scanTESS.sh
```
