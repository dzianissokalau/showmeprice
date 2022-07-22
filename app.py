from flask import Flask, render_template, request, make_response, redirect, send_from_directory
from data import data, columns_cities, columns_postcodes
from datetime import datetime, timedelta



app = Flask(__name__, static_folder='static')


@app.before_request
def before_request():
    if 'https://showmeprice.herokuapp.com/' in request.url or request.is_secure:
        url = request.url.replace('showmeprice.herokuapp.com', 'www.showmeprice.com', 1)
        url = request.url.replace('https://', 'http://', 1)
        code = 301
        return redirect(url, code=code)


@app.route('/', methods=['GET', 'POST'])
@app.route('/<deal_type>/<country>', methods=['GET', 'POST'])
def cities(deal_type='buy', country='uk'):
    table_header = columns_cities
    table_data = data[deal_type][country]['all']

    return render_template('table_cities.html', table_header=table_header, data=table_data, country=country, deal_type=deal_type)


@app.route('/<deal_type>/<country>/<city>', methods=['GET', 'POST'])
def postcodes(deal_type, country, city):
    table_header = columns_postcodes
    table_data = data[deal_type][country][city]

    return render_template('table_postcodes.html', table_header=table_header, data=table_data, country=country, city=city, deal_type=deal_type)


@app.route('/<deal_type>/<country>/<city>/<postcode>', methods=['GET', 'POST'])
def postcode(deal_type, country, city, postcode):
    table_header = columns_postcodes
    table_data = data[deal_type][country]['postcodes'][postcode]

    return render_template('table_postcode.html', table_header=table_header, data=table_data, country=country, city=city, postcode=postcode, deal_type=deal_type)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/sitemap', methods=['GET'])
@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    link = 'http://www.showmeprice.com'
    dt = (datetime.now() - timedelta(days=7)).date().isoformat()
    pages = []

    deal_types = data.keys()

    for deal_type in deal_types:
        countries = data[deal_type].keys()

        for country in countries:
            # add link for country
            pages.append([link + f'/{deal_type}/{country}', dt])

            cities = data[deal_type][country].keys()
            for city in cities:
                if city != 'all' and city != 'postcodes':
                    # add link for cities
                    pages.append([link + f'/{deal_type}/{country}/{city}', dt])

            postcodes = data[deal_type][country]['postcodes'].keys()
            for postcode in postcodes:
                if postcode != 'all':
                    city = data[deal_type][country]['postcodes'][postcode][0]['city']
                    # add link for cities
                    pages.append([link + f'/{deal_type}/{country}/{city}/{postcode}', dt])                  
    
        sitemap_xml = render_template('sitemap.xml', pages=pages)
        response = make_response(sitemap_xml)
        response.headers['Content-Type'] = 'application/xml'  

        return response


@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == '__main__':
    app.run(debug=False)