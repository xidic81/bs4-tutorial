import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detik_populer():
    html_doc = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'framebar'
                                                                        })
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    populer_area = soup.find(attrs={'grid-row list-content'})

    titles = populer_area.findAll(attrs={'media__title'})
    images = populer_area.findAll(attrs={'media__image'})

    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)