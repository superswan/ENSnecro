# ENSNecro
Dump all expired domains in the ENS Vision database for searching, sorting, etc.

```
curl 'https://dnlout9nnyfi.usemoralis.com:2053/server/classes/Names' \
  -H 'authority: dnlout9nnyfi.usemoralis.com:2053' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'content-type: text/plain' \
  -H 'origin: https://www.ens.vision' \
  -H 'referer: https://www.ens.vision/' \
  -H 'sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36' \
  --data-raw '{"where":{"categories":{"$nin":[99]},"name":{"$exists":true},"expiryDate":{"$gt":0,"$lt":1648563049.644}},"limit":65535,"order":"-expiryDate","_method":"GET","_ApplicationId":"MkQTnBTXRkHAoMZSYQyy1mzle70Bjih1LWEXXcue","_ClientVersion":"js1.7.0","_InstallationId":"596e6df9-5124-4543-a13c-34f3c12f6940"}' \
  --compressed
```




You can query the output using `jq`

`jq '.results[].name' ensvis.json | awk 'length($0) < 17'`