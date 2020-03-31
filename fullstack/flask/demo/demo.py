from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! World. World! Mwahaha! What the Heck!'

if __name__ == '__main__':
    # host param - Set this to '0.0.0.0' to have the server available externally as well. For the Vagrant VMbox forwarded_port to be accessible to the Host browser via localhost.
    # port param - the port of the webserver. Defaults to 5000 or the port defined in the SERVER_NAME config variable if present.
    # debug param - As such to enable just the interactive debugger without the code reloading, you have to invoke run() with debug=True and use_reloader=False.
    app.run(host='0.0.0.0', port=5000, debug=True)