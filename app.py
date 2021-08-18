from flask import Flask, render_template


# creates a Flask application, named app
app = Flask(__name__)


# add a simple POST method
@app.route('/api', methods = ['POST'])
def api():
    return '', 204


# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html')


# run the application
if __name__ == "__main__":
    app.run(debug=True)