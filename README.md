# metatron

Secure version control for metadata

See the [docs](docs/README.md).

## Getting started

Run IPFS server:
```
$ ipfs daemon
```

Start up redis:
```
sh start-redis.sh
```

Start up the Metatron vault:
```
sh run-vault.sh
```

Optionally run a scanner, e.g.:
```
sh scanTESS.sh
```

Navigate to http://localhost:5000
