from flask import Flask, jsonify, request
app = Flask(__name__)

application = app

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World!"

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    return jsonify({"result" : num*10})

if __name__ == '__main__':
    app.run(debug=True)