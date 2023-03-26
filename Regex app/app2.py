from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    test_string = request.form['test_string']
    regex = request.form['regex']
    matches = re.findall(regex, test_string)
    return render_template('test.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
 
