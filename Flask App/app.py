from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask Page"

@app.route('/upper')
def Upper():
    a = request.args.get('a')
    return a.upper()

@app.route('/lower')
def lower():
    a = request.args.get('a')
    return a.lower()
    

if __name__ == '__main__':
    app.run(debug=True)