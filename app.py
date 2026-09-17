from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>GST Invoice Generator</h1>
    <p>Application is under development.</p>
    <p>Invoice generation module coming soon.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
