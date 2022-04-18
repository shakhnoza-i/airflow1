import requests
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
        self.curr = 491

    def run(self, *args, **kwargs):
        date = datetime.today().strftime('%d.%m.%Y')
        r = requests.get('https://www.nationalbank.kz/rss/get_rates.cfm?fdate=%s' % date)
        login_page = r.text.encode('utf-8')
        soup = BeautifulSoup(login_page)
        desc = soup.find_all('description')
        self.curr = desc[12].text[0:-1]
        print(self.curr)
        return self.curr


app.register_task(CurrencyRate())