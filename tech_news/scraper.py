from parsel import Selector
import requests
import time
from bs4 import BeautifulSoup
import re


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
def get_tech_news(amount):
    """Seu código deve vir aqui"""
