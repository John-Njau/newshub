from flask import render_template,request,redirect,url_for
from app import web
from ..requests import get_source, get_news_articles, search_news

@web.route('/')
def index():
    title = "NewsHub"
    sources = get_source()
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',phrase=search_news))
    else:
        return render_template('index.html', title=title, sources=sources)

@web.route('/news/<id>')
def articles(id):
    title = "News Articles"
    articles = get_news_articles(id)
    return render_template('articles.html' , articles=articles, title=title)

@web.route('/news/<phrase>')
def search(phrase):
    phrase_list = phrase.split(" ")
    phrase_format = "+".join(phrase_list)
    searched_phrase = search_news(phrase_format)
    title = f'Results for {phrase}'
    return render_template('search.html', news = searched_phrase, title = title)