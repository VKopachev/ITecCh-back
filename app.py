from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/events', )
def get_events():
    events = [
        {
            'logo_img': 'https://scontent.fkbp1-1.fna.fbcdn.net/v/t1.0-9/18920261_1449723381732456_3126740517817752314_n.png?_nc_cat=106&_nc_ht=scontent.fkbp1-1.fna&oh=dd84db4fab57f8a71707452a072f7446&oe=5D544DE9',
            'company_name': 'InterLink LLC',
            'fb_company_link': 'https://www.facebook.com/interlinkua/',
            'img_link': 'https://scontent.fkbp1-1.fna.fbcdn.net/v/t1.0-9/59305857_2301256683245784_6300423410677710848_n.jpg?_nc_cat=104&_nc_ht=scontent.fkbp1-1.fna&oh=a4055400f9ec412f0a03b3eb0213600b&oe=5D666789',
            'date': '26.05.19',
            'title': 'InterLink Meetup: REST API - від проектування до тестування',
            'event_link': 'https://www.facebook.com/events/375193063338405/'
        },{
            'logo_img': 'https://scontent.fkbp1-1.fna.fbcdn.net/v/t1.0-9/18920261_1449723381732456_3126740517817752314_n.png?_nc_cat=106&_nc_ht=scontent.fkbp1-1.fna&oh=dd84db4fab57f8a71707452a072f7446&oe=5D544DE9',
            'company_name': 'InterLink LLC',
            'fb_company_link': 'https://www.facebook.com/interlinkua/',
            'img_link': 'https://scontent.fkbp1-1.fna.fbcdn.net/v/t1.0-9/56468288_2260478703990249_8621615095409016832_n.jpg?_nc_cat=109&_nc_ht=scontent.fkbp1-1.fna&oh=1f81136a62f51bb0e81eda31cb58d662&oe=5D9966CF',
            'date': '14.06.19',
            'title': 'InterLink Meetup: Everyday Git',
            'event_link': 'https://www.facebook.com/events/375282513201175/'
        },{
            'logo_img': 'https://scontent.fkbp1-1.fna.fbcdn.net/v/t1.0-9/18920261_1449723381732456_3126740517817752314_n.png?_nc_cat=106&_nc_ht=scontent.fkbp1-1.fna&oh=dd84db4fab57f8a71707452a072f7446&oe=5D544DE9',
            'company_name': 'InterLink LLC',
            'fb_company_link': 'https://www.facebook.com/interlinkua/',
            'img_link': 'https://scontent.fkbp1-1.fna.fbcdn.net/v/t1.0-9/52941744_2203681469669973_4932382331542437888_n.jpg?_nc_cat=109&_nc_ht=scontent.fkbp1-1.fna&oh=509e64d931e39f20e6cab59f94ceac5d&oe=5D5A25A1',
            'date': '28.03.19',
            'title': 'InterLink Meetup: Процес як інструмент дизайнера',
            'event_link': 'https://www.facebook.com/events/277441706483648/'
        }
    ]
    return jsonify(events)


if __name__ == '__main__':
    app.run()
