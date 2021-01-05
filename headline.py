from flask import Flask, render_template, request
import feedparser
app = Flask(__name__)
RSS_FEEDS = {'BBS':'http://feeds.bbci.co.uk/news/rss.xml',
            'CNN':'http://rss.cnn.com/rss/edition.rss',
            'FOX':'http://feeds.foxnews.com/foxnews/latest',
            'IOL':'http://www.iol.co.za/cmlink/1.640'}
@app.route('/') 
@app.route('/<publication>')
def get_news(publication='BBS'):
    query = request.args.get('publication')
    if not query or query.upper() not in RSS_FEEDS:
        publication = 'BBS'
    else:
        publication = query.upper()

