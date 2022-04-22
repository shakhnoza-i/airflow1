import requests
from bs4 import BeautifulSoup
from datetime import datetime
from celery import shared_task, Task


from core.celery import app
from airflow.models import ExchangeRate


@shared_task(bind=True)
def test_func(self):
    for i in range(1, 10):
        print(i)
    return "done"


@shared_task(bind=True)
def currency_rate(self, *args, **kwargs):
    date = datetime.today().strftime('%d.%m.%Y')
    r = requests.get('https://www.nationalbank.kz/rss/get_rates.cfm?fdate=%s' % date)
    login_page = r.text.encode('utf-8')
    soup = BeautifulSoup(login_page)
    desc = soup.find_all('description')
    curr = desc[12].text[0:-1]

    exchange = ExchangeRate.objects.create(
        currency = 'EUR',
        created_date = date,
        rate = curr
    )
    exchange.save()
    return curr
