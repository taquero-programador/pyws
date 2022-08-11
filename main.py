#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import csv
url = 'http://coreyms.com'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')

with open('corey.csv', 'w', newline='') as f:
    head_title = ['title', 'description', 'youtube-link']
    esc = csv.writer(f)
    esc.writerow(head_title)

    for article in soup.find_all('article'):
        head = article.h2.a.text
        print(head)
        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']
            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]
            yt_link = f"https://youtube.com/watch?v={vid_id}"
        except Exception as e:
            yt_link = None
        print(yt_link)
        print()
        esc.writerow([head, summary, yt_link])
