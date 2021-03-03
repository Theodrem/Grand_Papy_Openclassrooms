from flask import render_template, request, jsonify

from app import app
from app.parser import Parser
from app.api.gecoding import Geocoding
from app.api.wiki import Wiki
from app.message import get_message, get_end_message, get_errors_response


@app.route('/')
def index():
    """
    :return: The template of the index website
    """
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    """

    :return:
    User input,
    latitude,
    longitude,
    location address,
    Grand py message,
    Grand py end message,
    MediaWiki description

    """
    user_input = request.form.get('input_user')  # Take user input
    sentence = Parser(user_input)  # Create a parser instance
    parsed_input = sentence.transform_input()  # This variable is final input

    try:
        geo = Geocoding(parsed_input)  # Try to create a geocoding instance
        lng = geo.get_longitude()
        lat = geo.get_latitude()
        address = geo.get_address()
        message = None
        end_message = None
        wiki = Wiki(lat, lng)  # Try to create a wiki instance

        try:
            mess_wiki = wiki.get_description()  # Try to get data from mediaWiki
            message = get_message()
            end_message = get_end_message()

        except IndexError:
            mess_wiki = get_errors_response(
                "no_found_wiki")  # Error message wiki

    except IndexError:
        """
        Have to declare all the variables to avoid the 500 error
        """
        address = None
        lng = None
        lat = None
        mess_wiki = None
        message = get_errors_response(
            "no_found_mess")  # Error message geocoding
        end_message = None

    return jsonify({'input_user': parsed_input, 'lat': lat, 'lng': lng,  # Return all data with json format
                    'address': address, "message": message,
                    'end_mess': end_message, 'wiki': mess_wiki})


@app.errorhandler(404)
def resource_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def error_networks(e):
    return render_template("500.html")
# https://validator.w3.org/
