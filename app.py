import os
from flask import Flask, render_template, request
# from azure.monitor.opentelemetry import configure_azure_monitor

app = Flask(__name__)

# configure_azure_monitor will automatically look for
# APPLICATIONINSIGHTS_CONNECTION_STRING in the environment if not specified.
# By enabling live metrics, you get real-time analytics.
# configure_azure_monitor(
#     enable_live_metrics=True
    # No need to pass connection_string here as it will be taken from env var
# )

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




if __name__ == "__main__":
    app.run(debug=True)
