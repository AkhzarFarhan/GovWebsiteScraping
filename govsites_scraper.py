# -*- coding: utf-8 -*-
"""GovSites-Scraper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EO8a19JmFaxV1ZVACUQiIpJM3okNU6s3
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

"""#Land Revenue Bihar"""

data = []
for i in range(1,136,1):
    payload = {"dst_id":"7","c_id":"7","h_id":"19","m_id":"18","btnType":"pan","btn_request":"खोजे"}
    page = requests.get('http://www.bhulagan.bihar.gov.in/Citizen/search.aspx?page={i}'.format(i=i), params=payload)
    soup = BeautifulSoup(page.content, 'html.parser')

    soup_output = soup.find('table')
    rows = soup_output.find_all('tr')
    for row in rows[1:]:
        d_row = []
        for r in row.find_all('td')[:-1]:
            d_row.append(r.contents[0].encode('raw-unicode-escape').decode('utf-8', 'replace'))
            # print(r.contents[0].encode('raw-unicode-escape').decode('utf-8', 'replace'))
        d_row.append('http://www.bhulagan.bihar.gov.in/Citizen/' + row.find('a')['href'])
        # print('http://www.bhulagan.bihar.gov.in/Citizen/' + row.find('a')['href'])
        data.append(d_row)
data

df = pd.DataFrame(data)
df.to_csv('/content/drive/My Drive/Revenue/Record2.csv', index=False, header=['Serial No', 'Name', 'Account No', 'Current Part', 'Current Page No', 'URL'])

df.tail()

