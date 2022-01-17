from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return render_template("home.html", message="In what town do you want rest Hunter ?")

@app.route("/town", methods=['GET','POST'])
def town():
    text = request.form['text']
    processed_text = "Welcome to " + text.upper() + " Hunter."
    return render_template("page_suivante.html",message = processed_text)

if __name__ == "__main__":
    app.run(debug=True)