from datetime import datetime
from requests_html import HTMLSession
url = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&aqs=chrome..69i57j0l7.6426j1j4&sourceid=chrome&ie=UTF-8'
session = HTMLSession()
response = session.get(url)
title = response.html.xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
currency = str(title)[-11:-6]
with open('tro.txt', 'a') as f:
    f.write(f'{datetime.now()} - курс доллара - {currency}\n')
