import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTkyLjE2OC4xNS42MC9hcGkvdjEvYXV0aC9sb2dpbiIsImlhdCI6MTY4NTUzNTk3NywiZXhwIjoxNjg1NTc5MTc3LCJuYmYiOjE2ODU1MzU5NzcsImp0aSI6IkEwZHcwQWdHeUFLdEZGYVEiLCJzdWIiOjI0NzMsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.i9mtWmozbwUpKjIoL3kcL7Sc3_EIYGNfwxPZMUeEff4',
    'Connection': 'keep-alive',
    'Origin': 'http://192.168.15.50',
    'Referer': 'http://192.168.15.50/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-RED-HID': '2',
}

params = (
    ('id', '178530'),
    ('phongId', '828'),
    ('benhVienId', '2'),
    ('type', 'NOI_TRU'),
)

response = requests.get('http://192.168.15.60/api/v1/dontiep/getHsbaByHsbaId', headers=headers, params=params, verify=False)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://192.168.15.60/api/v1/dontiep/getHsbaByHsbaId?id=178530&phongId=828&benhVienId=2&type=NOI_TRU', headers=headers, verify=False)
print(response.json())