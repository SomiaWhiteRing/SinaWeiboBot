from apscheduler.schedulers.blocking import BlockingScheduler

from weibo import WeiboClient
from func.poemFunc import poemFunc

if __name__ == '__main__':
    with open('./data/access_token.txt', 'rt') as f:
        access_token = f.read()
    client = WeiboClient(access_token)
    scheduler = BlockingScheduler()
    poem_hour_fun = poemFunc(client, './data/poem.json')
    scheduler.add_job(poem_hour_fun.do, 'cron', second='*/1')
    scheduler.start()
