from parsel import Selector
import requests
import time
from bs4 import BeautifulSoup
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except requests.exceptions.ReadTimeout:
        return None
    except requests.exceptions.HTTPError:
        return None
    else:
        time.sleep(1)
        return response.text


# Requisito 2
def scrape_updates(html):
    selector = Selector(text=html)
    news_links = selector.css('.entry-title a::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_link = soup.find("a", class_="next page-numbers")
    if next_link:
        return next_link["href"]
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    url = soup.find('link', rel='canonical')['href']
    title = soup.find('h1', class_='entry-title').text.strip()
    timestamp = soup.find('li', class_='meta-date').text.strip()
    writer = soup.find('a', class_='url fn n').text.strip()
    reading_time = int(re.findall(r'\d+', soup.find(
        'li', class_='meta-reading-time').text)[0])
    summary = soup.find('div', class_='entry-content').p.text.strip()
    category = soup.find('span', class_='label').text.strip()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(n):
    response_fetch = fetch("https://blog.betrybe.com/")
    get_all_links = scrape_updates(response_fetch)
    get_next_link = scrape_next_page_link(response_fetch)
    while len(get_all_links) < n:
        get_next_response_fetch = fetch(get_next_link)
        new_response_fetch_links = scrape_updates(get_next_response_fetch)
        get_all_links.extend(new_response_fetch_links)
        get_next_link = scrape_next_page_link(get_next_response_fetch)
    new_response = [scrape_news(fetch(link)) for link in get_all_links[:n]]
    return create_new_response_db(new_response)


def create_new_response_db(new_response):
    create_news(new_response)
    return new_response
