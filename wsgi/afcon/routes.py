from afcon.core import app


@app.route('/')
def dragons():
    return "Here be dragons! (and an API)"
