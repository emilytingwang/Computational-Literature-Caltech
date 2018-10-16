# Notes: This framework uses the templates EmilyWang_home.html as the homepage, and EmilyWang_transformed.html
# to display the new text, transformed (editable).
# Original template file in textbook used TextBlob, check it out?

# virtualenv venv
# venv\Scripts\activate.bat
# http://localhost:5000/

from flask import Flask, request, render_template
import random

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("EmilyWang_home.html")

@app.route('/transformed', methods=["POST"])
def transformed():
    text = request.form['text']
    return render_template("EmilyWang_transformed.html", text=text)

if __name__ == '__main__':
    app.run()