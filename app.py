from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/contact")
def contact():
    return render_template("Contact.html")

@app.route('/fake_submit', methods=['POST'])
def fake_submit():
    # Return a simple success response
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
