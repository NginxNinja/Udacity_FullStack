from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Welcome1@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

# db.create_all() //This method can only be used if not using the Flask-Migrate library.

@app.route('/todo/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        abort(400)
    else:
        return jsonify(body)

''' # Original version without handling sessions in controllers using try/except/finally blocks
def create_todo():
    #description = request.form.get('description', '') // the original request.form object without calling JSON
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()

    #return redirect(url_for('index')) // the original code without using JSON
    return jsonify({
        'description': todo.description
    })
'''

@app.route('/todo/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed = request.get_json()['completed']
        print('completed', completed)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())

if __name__ == '__main__':
    # host param - Set this to '0.0.0.0' to have the server available externally as well. For the Vagrant VMbox forwarded_port to be accessible to the Host browser via localhost.
    # port param - the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present.
    # debug param - As such to enable just the interactive debugger without the code reloading, you have to invoke run() with debug=True and use_reloader=False.
    app.run(host='0.0.0.0', port=5000, debug=True)