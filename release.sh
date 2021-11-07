#!/bin/bash

DATE=`date +%y.%m.%d`
VERSION="v$DATE"
OWNER=cryptotechguru

sh updateVersion.sh

sh buildVault.sh
docker tag metatron-vault ghcr.io/$OWNER/metatron-vault:latest
docker push ghcr.io/$OWNER/metatron-vault:latest
docker tag metatron-vault ghcr.io/$OWNER/metatron-vault:$VERSION
docker push ghcr.io/$OWNER/metatron-vault:$VERSION

sh buildScanner.sh
docker tag metatron-scanner ghcr.io/$OWNER/metatron-scanner:latest
docker push ghcr.io/$OWNER/metatron-scanner:latest
docker tag metatron-scanner ghcr.io/$OWNER/metatron-scanner:$VERSION
docker push ghcr.io/$OWNER/metatron-scanner:$VERSION
