from flask import Flask, render_template, request
from data import data, columns_cities, columns_postcodes


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)