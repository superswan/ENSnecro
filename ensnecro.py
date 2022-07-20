import requests

def dump_database():
    headers = {
        'authority': 'dnlout9nnyfi.usemoralis.com:2053',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'text/plain',
        'origin': 'https://www.ens.vision',
        'referer': 'https://www.ens.vision/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = '{"where":{"categories":{"$nin":[99]},"name":{"$exists":true},"expiryDate":{"$gt":0,"$lt":1648563049.644}},"limit":500000,"order":"-expiryDate","_method":"GET","_ApplicationId":"MkQTnBTXRkHAoMZSYQyy1mzle70Bjih1LWEXXcue","_ClientVersion":"js1.7.0","_InstallationId":"596e6df9-5124-4543-a13c-34f3c12f6940"}'

    print("Fetching DB")
    response = requests.post('https://dnlout9nnyfi.usemoralis.com:2053/server/classes/Names', headers=headers, data=data)

    print("Exporting to json")
    with open ('ensvis-yuge.json', 'wb') as dbfile:
        dbfile.write(response.content)

dump_database()