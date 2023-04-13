from parsel import Selector
import requests
import time
# from bs4 import BeautifulSoup


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
    news_links = selector.css('.entry-title::attr(href)').getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
