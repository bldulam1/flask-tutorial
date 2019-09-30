from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/about')
def about_page():
    print(request.args.get("n"))
    return 'About Page'

if __name__ == '__main__':
    app.run(debug=True)