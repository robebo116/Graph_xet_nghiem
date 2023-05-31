# import requests

# headers = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
#     'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTkyLjE2OC4xNS42MC9hcGkvdjEvYXV0aC9sb2dpbiIsImlhdCI6MTY4NTQ5MDU0OSwiZXhwIjoxNjg1NTMzNzQ5LCJuYmYiOjE2ODU0OTA1NDksImp0aSI6IkE1T2NFTFY0WWVsMFVWTWgiLCJzdWIiOjI0NzMsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.J_webKe8JCBLjBZP5TZu9NgeM1uwSDMaXlil8b29Ztc',
#     'Connection': 'keep-alive',
#     'Origin': 'http://192.168.15.50',
#     'Referer': 'http://192.168.15.50/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#     'X-RED-HID': '2',
# }

# response = requests.get('http://192.168.15.60/api/v1/phongkham/getDetailPhieuYLenh/1454324/2', headers=headers, verify=False)
import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vMTkyLjE2OC4xNS42MC9hcGkvdjEvYXV0aC9sb2dpbiIsImlhdCI6MTY4NTQ5MDU0OSwiZXhwIjoxNjg1NTMzNzQ5LCJuYmYiOjE2ODU0OTA1NDksImp0aSI6IkE1T2NFTFY0WWVsMFVWTWgiLCJzdWIiOjI0NzMsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.J_webKe8JCBLjBZP5TZu9NgeM1uwSDMaXlil8b29Ztc',
    'Connection': 'keep-alive',
    'Origin': 'http://192.168.15.50',
    'Referer': 'http://192.168.15.50/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'X-RED-HID': '2',
}

response = requests.get('http://192.168.15.60/api/v1/phongkham/getDetailPhieuYLenh/1454348/2', headers=headers, verify=False)
x = response.json()
for i in range(len(x)):
    try:
        x[i]['thoi_gian_chi_dinh']
        print('NO')
    except:
        ten = x[i]['ten']
        with open('ds_ten_xn.txt','a',encoding='utf-8') as file:
            file.write(ten)
            file.write('\n')