from collections import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    categories = [news['category'] for news in find_news()]
    if not categories:
        return []
    counts_news_category = Counter(categories)
    top_categories = sorted(
        counts_news_category.items(),
        key=lambda x: (-x[1], x[0].lower())
    )
    return [category for category, _ in top_categories[:5]]
