from afcon import app

@app.route('/')
def index():
    return "Here be dragons! (and an API)"