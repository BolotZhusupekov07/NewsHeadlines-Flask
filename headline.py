from flask import Flask
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
    first_article = FEED['entries'][0]
    return """ <html>
        <body>
            <h1> Headlines </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
        </html>""".format(first_article.get('title'), first_article.get('published'), first_article.get('summary'))


if __name__ == '__main__':
    app.run(port = 5000, debug=True)