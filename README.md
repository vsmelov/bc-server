# bc-server

### build
```bash
docker build -t bcserver .
```

### run
```bash
docker run --rm -ti -p 127.0.0.1:8000:8000/tcp --name bcserver bcserver
```

### use
```bash
curl -X GET "http://127.0.0.1:8000/nft/hasNFT?wallet=0x37bFa1452BE9676992027Ac4172a7d1141335B5b&nftId=4"
```