from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # CORS app
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    CORS(app)

    # CORS headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/messages')
    @cross_origin() # needs to be imported from flask_cors module
    def get_messages():
        return 'GETTING MESSAGES'

    @app.route('/')
    def hello_world():
        return jsonify({'message': 'HELLO WORLD'})

    return app

""" if __name__ == '__main__':
    # Run these commands in CLI for the alternative of this method.
    # export FLASK_APP=<filename.py>
    # export FLASK_ENV=development
    # host param can be run in CLI like this => flask run --host=0.0.0.0
    app.run(host = '0.0.0.0', port = 5000, debug = True) """