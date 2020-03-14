import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>flask api Reading Archive</h1><p>This site is a prototype API for flask reading of novels.</p>"

app.run()