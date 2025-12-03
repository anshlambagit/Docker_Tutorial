from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask App running in Docker!"

@app.route("/about")
def about():
    return "This is a simple Flask application running inside a Docker container."

@app.route("/contact")
def contact():
    return "Contact us at: abc"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)