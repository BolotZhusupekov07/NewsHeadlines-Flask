from flask import Flask, render_template, request
import feedparser
import json
from urllib.request import urlopen
import urllib.parse

app = Flask(__name__)
RSS_FEEDS = {'BBS':'http://feeds.bbci.co.uk/news/rss.xml',
            'CNN':'http://rss.cnn.com/rss/edition.rss',
            'FOX':'http://feeds.foxnews.com/foxnews/latest',
            'IOL':'http://www.iol.co.za/cmlink/1.640'}

DEFAULTS = {"publication": 'BBS', "city": 'London, UK'}

@app.route('/') 
def home():
    publication = request.args.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)
    return render_template('home.html', articles=articles, weather = weather)
def get_news(query):
    query = request.args.get('publication')
    if not query or query.upper() not in RSS_FEEDS:
        publication = 'BBS'
    else:
        publication = query.upper()
    FEED = feedparser.parse(RSS_FEEDS[publication])
    return FEED['entries']
   
def get_weather(query):
    query = urllib.parse.quote(query)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dc5d0055ebc9dd6af11cda49ae915189'.format(query)
    
    
    data = urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":parsed["weather"][0]["description"],
                    "temperature":parsed["main"]["temp"],
                    "city":parsed["name"], 
                    'country': parsed['sys']['country']
                    }
    return weather



if __name__ == '__main__':
    app.run(port = 5000, debug=True)

