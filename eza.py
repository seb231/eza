import requests
import re
import datetime
from bs4 import BeautifulSoup

patreon_content = requests.get('https://www.patreon.com/EasyAllies').content
patreon_soup = BeautifulSoup(patreon_content, "lxml")

main_content = patreon_soup.find('body').find('script').text

def search_patreon_content(term, content):
    search = re.findall(r'\b\d+\b', str(re.search(str(term + '.*(?:,)'), content)).split()[-1])
    return search

patron_count = search_patreon_content('patron_count', main_content)
patreon_sum = search_patreon_content('pledge_sum', main_content)

print(patron_count + patreon_sum)

now = datetime.datetime.now()
now.isoformat()

eza_content = requests.get('https://www.youtube.com/channel/UCZrxXp1reP8E353rZsB3jaA/videos').content
eza_soup = BeautifulSoup(eza_content, "lxml")

titles = []

video_content = eza_soup.find_all('a', attrs = {'class': 'yt-uix-sessionlink yt-uix-tile-link spf-link yt-ui-ellipsis yt-ui-ellipsis-2'})

for title in video_content:
    titles.append(title.get_text())

print(titles)


