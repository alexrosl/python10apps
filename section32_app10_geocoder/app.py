from datetime import datetime

from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas


app = Flask(__name__)
global filename

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success-table", methods=["POST"])
def success_table():
    global filename
    if request.method == "POST":
        file = request.files["file"]
        try:
            df = pandas.read_csv(file)
            gc = Nominatim()
            df["coordinates"] = df["Address"].apply(gc.geocode)
            df["Latitude"] = df["coordinates"].apply(lambda x: x.latitude if x is not None else None)
            df["Longitude"] = df["coordinates"].apply(lambda x: x.longitude if x is not None else None)
            df = df.drop("coordinates", 1)
            filename = datetime.now().strftime("uploads/%Y-%m%d-%H-%M-%S-%f"+".csv")
            df.to_csv(filename, index=None)
            return render_template("index.html", text=df.to_html(), btn="download.html")
        except:
            return render_template("index.html", text="Please make sure you have an address column in your CSV file")


@app.route("/download-file")
def download():
    return send_file(filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)