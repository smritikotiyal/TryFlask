from flask import Flask, jsonify, request
application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World!"

@application.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({"result" : num*10})

if __name__ == '__main__':
    application.run(debug=True)