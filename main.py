from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="")

@app.route('/cards', methods=['GET', 'POST'])
def cards():
    return render_template("cards.html", title="")

@app.route('/map', methods=['GET', 'POST'])
def cards():
    return render_template("map.html", title="")


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1', threaded=True)
