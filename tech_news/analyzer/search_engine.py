from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(n["title"], n["url"]) for n in search_news(query)]


# Requisito 8
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    date_formatting = datetime.strptime(
        date, '%Y-%m-%d').strftime('%d/%m/%Y')
    news = search_news({'timestamp': {'$eq': date_formatting}})
    return [(new['title'], new['url']) for new in news]


# Requisito 9
def search_by_category(category):
    query = {"categories": {"$regex": category.capitalize()}}
    return [(n["title"], n["url"]) for n in search_news(query)]
