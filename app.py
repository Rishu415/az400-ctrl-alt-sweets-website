import os
from flask import Flask, render_template, request
from azure.monitor.opentelemetry import configure_azure_monitor

app = Flask(__name__)

configure_azure_monitor(
    connection_string="InstrumentationKey=337a63d2-a7d7-4c24-bac5-eccde6c06242;IngestionEndpoint=https://eastus2-3.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus2.livediagnostics.monitor.azure.com/;ApplicationId=0ffaabbc-c09a-493c-a962-8a33860224c8",
    enable_live_metrics=True
)

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
