import flask

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/env')
def env():
    lines = [
        "{} => {}".format(key, value)
        for key, value
        in flask.request.environ.items()
    ]

    return Response(
        "\n".join(lines),
        content_type="text/plain;charset=UTF-8"
    )

if __name__ == "__main__":
    app.run()

