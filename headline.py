from flask import Flask, render_template
import feedparser
app = Flask(__name__)
RSS_FEEDS = {'BBS':'http://feeds.bbci.co.uk/news/rss.xml',
            'CNN':'http://rss.cnn.com/rss/edition.rss',
            'FOX':'http://feeds.foxnews.com/foxnews/latest',
            'IOL':'http://www.iol.co.za/cmlink/1.640'}
@app.route('/') 
@app.route('/<publication>')
def get_news(publication='BBS'):
    FEED = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html', articles=FEED['entries'])


if __name__ == '__main__':
    app.run(port = 5000, debug=True)
