from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Welcome1@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class TodoList(db.Model):
    ''' This is the Parent Model '''
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    
    # 1st param = Class name passed as String
    # 2nd param = customize name for referencing into the Child Table
    # 3rd param = a method of Relationship Loading Technique
    todos = db.relationship('Todo', backref='list', lazy=True)

    def __repr__(self):
        return f'<TodoList id:{self.id} name:{self.name}>'

class Todo(db.Model):
    ''' This is the Child Model '''
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey('todolist.id'), nullable=False)

    def __repr__(self):
        return f'<Todo id:{self.id} {self.description} list:{self.list_id}>'

# db.create_all() //This method can only be used if not using the Flask-Migrate library.

@app.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        Todo.query.filter_by(id=todo_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({ 'success': True })

@app.route('/todo/create', methods=['POST'])
def create_todo():
    error = False
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description=description)
        db.session.add(todo)
        db.session.commit()
        body['id'] = todo.id
        body['completed'] = todo.completed
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

''' # The Original version without handling sessions in controllers using try/except/finally blocks
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