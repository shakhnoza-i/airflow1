import requests
import lxml.html
from bs4 import BeautifulSoup
from datetime import datetime
from celery import shared_task, Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
from core.celery import app

@shared_task(bind=True)
def test_func(self):
    for i in range(1, 10):
        print(i)
    return "done"

class CurrencyRate(Task):
    def __init__(self):
        self.curr = 10
        print(self.curr)
    def run(self, *args, **kwargs):
        date = datetime.today().strftime('%d.%m.%Y')
        r = requests.get('https://www.nationalbank.kz/rss/get_rates.cfm?fdate=%s' % date)
        # self.curr += 1
        # logger.info(self.curr)
        login_page = r.text.encode('utf-8')
        doc = lxml.html.fromstring(login_page)
        self.curr = doc.xpath('/rates/item[12]/description')

        print(self.curr)
        return date


app.register_task(CurrencyRate())