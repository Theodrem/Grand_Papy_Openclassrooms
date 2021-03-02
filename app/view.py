from flask import render_template, request, jsonify

from app import app
from app.parser import Parser
from app.api.gecoding import Geocoding
from app.api.wiki import Wiki
from app.message import get_message, get_end_message, get_errors_response



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form.get('input_user')
    sentence = Parser(user_input)
    parsed_input = sentence.transform_input()

    try:
        geo = Geocoding(parsed_input)
        lng = geo.get_longitude()
        lat = geo.get_latitude()
        address = geo.get_address()
        message = None
        end_message = None
        wiki = Wiki(lat, lng)

        try:
            mess_wiki = wiki.get_description()
            message = get_message()
            end_message = get_end_message()

        except IndexError:
            mess_wiki = get_errors_response("no_found_wiki")

    except IndexError:
        address = None
        lng = None
        lat = None
        mess_wiki = None
        message = get_errors_response("no_found_mess")
        end_message = None

    return jsonify({'input_user': parsed_input, 'lat': lat, 'lng': lng,
                    'address': address, "message": message,
                    'end_mess': end_message, 'wiki': mess_wiki})




#https://validator.w3.org/

