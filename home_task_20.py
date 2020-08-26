#!/usr/local/bin python3
import asyncio
import aiohttp
import json


async def request_data(reddit):
    url = f'https://www.reddit.com/r/{reddit}/hot.json?limit=5'
    async with aiohttp.request('GET', url) as resp:
        return await resp.json()

async def main():
    reddits = {
            'python',
            'compsci', 
            'microbork',
        }
    res = await asyncio.gather(*(request_data(redd) for redd in reddits))
    data = [x for x  in res] 
    data_reddits = dict()
    for i in data:
        data_reddits[i['data']['children'][0]['data']['subreddit']] = dict()
        for j in  i['data']['children']:
            data_reddits[i['data']['children'][0]['data']['subreddit']][j['data']['title']] = {
                    'score' : j['data']['score'],
                    'link' : j['data']['permalink']
                    }
asyncio.run(main())
