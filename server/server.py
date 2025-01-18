from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'message': 'This is a simple Flask endpoint',
        'status': 'success'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)