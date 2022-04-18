from celery import shared_task, Task
import requests
from datetime import datetime
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
        # date = datetime.today().strftime('%d.%m.%Y')
        # req1 = requests.post('https://www.nationalbank.kz/rss/get_rates.cfm?fdate=%s' % date).json()
        self.curr += 1
        logger.info(self.curr)
        return self.curr


app.register_task(CurrencyRate())