import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import random

from .models import setup_db, Book

BOOKS_PER_SHELF = 8

def paginate_books(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * BOOKS_PER_SHELF
    end = start + BOOKS_PER_SHELF

    books = [book.format() for book in selection]
    current_books = books[start:end]

    return current_books

def create_app(test_config=None):
    ''' create and configure the app '''
    app = Flask(__name__)
    # app = Flask(__name__, instance_relative_config=True)
    # CORS app
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/messages')
    @cross_origin() # needs to be imported from flask_cors module
    def get_messages():
        return 'GETTING MESSAGES'

    @app.route('/books')
    def retrieve_books():
        selection = Book.query.order_by(Book.id).all()
        current_books = paginate_books(request, selection)

        if len(current_books) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'books': current_books,
            'total_books': len(Book.query.all())
        })

    @app.route('/books/<int:book_id>', methods=['PATCH'])
    def update_book(book_id):
        body = request.get_json()

        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()
            if book is None:
                abort(404)

            if 'rating' in body:
                book.rating = int(body.get('rating'))

            book.update()

            return jsonify({
                'success': True,
            })
        except:
            abort(400)

    @app.route('/books/<int:book_id>', methods=['DELETE'])
    def delete_book(book_id):
        try:
            book = Book.query.filter(Book.id == book_id).one_or_none()

            if book is None:
                abort(404)

            book.delete()
            selection = Book.query.order_by(Book.id).all()
            current_books = paginate_books(request, selection)

            return jsonify({
                'success': True,
                'deleted': book_id,
                'books': current_books,
                'total_books': len(Book.query.all())
            })
        except:
            abort(422)

    @app.route('/books', methods=['POST'])
    def create_book():
        body = request.get_json()

        new_title = body.get('title', None)
        new_author = body.get('author', None)
        new_rating = body.get('rating', None)
        search = body.get('search', None)

        try:
            if search:
                selection = Book.query.order_by(Book.id).filter(Book.title.ilike('%{}%'.format(search)))
                current_books = paginate_books(request, selection)

                return jsonify({
                    'success': True,
                    'books': current_books,
                    'total_books': len(selection.all())
                })

            else:
                book = Book(title=new_title, author=new_author, rating=new_rating)
                book.insert()

                selection = Book.query.order_by(Book.id).all()
                current_books = paginate_books(request, selection)

                import pdb; pdb.set_trace()

                return jsonify({
                    'success': True,
                    'created': book.id,
                    'books': current_books,
                    'total_books': len(Book.query.all())
                })
        except:
            abort(422)

# # The original version before adding the 'search' entry.
#     @app.route('/books', methods=['POST'])
#     def create_book():
#         body = request.get_json()

#         new_title = body.get('title', None)
#         new_author = body.get('author', None)
#         new_rating = body.get('rating', None)

#         try:
#             book = Book(title=new_title, author=new_author, rating=new_rating)
#             book.insert()

#             selection = Book.query.order_by(Book.id).all()
#             current_books = paginate_books(request, selection)

#             import pdb; pdb.set_trace()

#             return jsonify({
#                 'success': True,
#                 'created': book.id,
#                 'books': current_books,
#                 'total_books': len(Book.query.all())
#             })
#         except:
#             abort(422)

    @app.route('/')
    def hello_world():
        return jsonify({'message': 'HELLO WORLD'})

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    return app

""" if __name__ == '__main__':
    # Run these commands in CLI for the alternative of this method.
    # export FLASK_APP=<filename.py>
    # export FLASK_ENV=development
    # host param can be run in CLI like this => flask run --host=0.0.0.0
    app.run(host = '0.0.0.0', port = 5000, debug = True) """