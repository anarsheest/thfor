import flask

app = flask.App()

@app.route("/")
def index():
	return flask.render_template("index.html")

if __name__ == "__main__":
	app.run()