from flask import Flask, request
from PIL import Image
import pytesseract
import time
import io


app = Flask(__name__)


JWT_WHITE_LIST = [
    'fda9c8212cc249088ba680e013ed8ec8',
]


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        # return 401 if token is not passed
        if not token:
            return {'code': 401, 'message' : 'Token is missing !!'}
        # check jwt token in JWT_WHITE_LIST
        jwt_header_flag, token = token.split(' ') # JWT xxxx
        if token in JWT_WHITE_LIST:
            return f(*args, **kwargs)
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            # check for this decoded data
            return {'code': 401, 'message' : 'Token is missing !!'}
        except:
            return {'code': 401, 'message' : 'Token is invalid !!'}
        return  f(*args, **kwargs)
    return decorated


@app.route('/')
def index():
    return "Hello, This is a simple OCR recognizer server!"


@app.route('/recognize', methods=['POST'])
def reconize():
    stream = io.BytesIO(request.data)
    image = Image.open(stream)
    text = pytesseract.image_to_string(image)
    return {'code': 200, 'data': text}


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8558, debug=False)

