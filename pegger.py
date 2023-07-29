import xidb
from authorize import Authorizer
import os

cid = 'QmdtqspZvRCemuJqqYA5336jxj1kZ95GwP2kDdcpksVVTc'
cid = 'QmZmYF34urj55eXQVe56zitmKeTxZQrLGF5atdHgGbDdof'
cid = 'QmQM8bNoR4yT1qFYHQcCpxDa6K1Qavv3AYQ9UZt1iP2aPF'
xid = xidb.getXid(cid)
print(xid)

os.environ['TESS_CONNECT'] = 'http://scully:sw33tp0tat0@localhost:8337'
authorizer =  Authorizer('TESS')
authorizer.updateWallet()
balance = authorizer.getBalance()
print(balance)
txid = authorizer.authorize(cid)
print(txid)

print(xidb.encodeCid(cid))
print(xidb.getXid(cid))
print(xidb.getMeta(cid))

for asset in authorizer.assets:
    print(asset.xid)
    print(asset.cid)
    print(asset.tx['txid'])
    print(asset.tx['vout'][0]['scriptPubKey']['asm'])
