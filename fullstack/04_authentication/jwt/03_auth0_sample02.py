from flask import Flask, request, abort
from functools import wraps

app = Flask(__name__)

def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)

    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')

    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() != 'bearer':
        abort(401)

    return header_parts[1]

def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)
    return wrapper

@app.route('/headers')
@requires_auth
def headers(jwt):
    # @TODO unpack the request header
    
    print(jwt)
    return 'not implemented'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)