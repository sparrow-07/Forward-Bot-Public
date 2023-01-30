from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'https://www.youtube.com'


if __name__ == "__main__":
    app.run()
