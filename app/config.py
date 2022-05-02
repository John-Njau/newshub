class Config:
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True