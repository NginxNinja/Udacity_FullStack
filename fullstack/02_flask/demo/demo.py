from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vagrant:Welcome1@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return f'Hello, {person.name}!'

if __name__ == '__main__':
    # host param - Set this to '0.0.0.0' to have the server available externally as well. For the Vagrant VMbox forwarded_port to be accessible to the Host browser via localhost.
    # port param - the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present.
    # debug param - As such to enable just the interactive debugger without the code reloading, you have to invoke run() with debug=True and use_reloader=False.
    app.run(host='0.0.0.0', port=5000, debug=True)