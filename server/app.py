#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound

from models import db, Foods, Login, User, Driver

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

@app.errorhandler(NotFound)
def handle_not_found(e):
    response = make_response("Not Found: The requested resource not found", 404)
    return response

@app.route('/')
def home():
    return 'Flask Code Challenge Week Two'

@app.route('/get_driver_name', methods=['GET'])
def get_driver_name():
    # Assuming you have a Drivers table/model with a column 'name'
    driver = Driver.query.first()
    if driver:
        return jsonify({'driver_name': driver.name})
    else:
        return jsonify({'driver_name': 'Unknown'})

class FoodsPages(Resource):
    def get(self):
        response_dict = [n.to_dict() for n in Foods.query.all()]
        response = make_response(jsonify(response_dict), 200)
        return response

class FoodsById(Resource):
    def get(self, id):
        record = Foods.query.filter_by(id=id).first()
        if record is None:
            response = make_response(jsonify({'error': 'Home page not found'}), 404)
            return response
        else:
            record_dict = record.to_dict()
            response = make_response(record_dict, 200)
            return response

    def delete(self, id):
        home_page = Foods.query.filter_by(id=id).first()
        if home_page is None:
            response = make_response(jsonify({'error': 'Home page not found'}), 404)
            return response
        db.session.delete(home_page)
        db.session.commit()

class SearchIcons(Resource):
    def get(self):
        response_dict = [n.to_dict() for n in SearchIcon.query.all()]
        if len(response_dict) == 0:
            response = make_response("Search icons not found", 404)
            return response
        else:
            response = make_response(jsonify(response_dict), 200)
            return response

class LoginResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            login = Login.query.filter_by(email=email).first()
            if not login:
                return make_response(jsonify({"error": "Login not found"}), 404)

            if login.password != password:
                return make_response(jsonify({"error": "Password is incorrect"}), 401)

            user = User.query.filter_by(login_id=login.id).first()
            response_dict = user.to_dict()
            response = make_response(jsonify(response_dict), 200)
            return response

        except:
            error_dict = {"errors": ["validation errors"]}
            response = make_response(error_dict, 404)
            db.session.rollback()
            return response

# Api routes
api.add_resource(FoodsPages, '/foods')
api.add_resource(FoodsById, '/foods/<int:id>')
api.add_resource(SearchIcons, '/search_icons')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(port=5555, debug=True)