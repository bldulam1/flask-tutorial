from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/about')
def about_page():
    return 'About Page'

if __name__ == '__main__':
    app.run(debug=True)