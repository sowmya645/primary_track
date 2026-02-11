from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def hom():
    return "Hello, flask!"

@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}"

@app.route("/about")
def checkt():
    return render_template("index.html", name="sam")

@app.route("/for")
def fors():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    return f"username {username}"

@app.route("/sla")
def home():
    return render_template("slay.html")

# ✅ Fixed decorator here
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file and file.filename:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)
        image_url = url_for("static", filename=file.filename)
        return f"""
        <h2>Uploaded Image:</h2>
        <img src="{image_url}" alt="Uploaded Image" width="300">
        """
    return "No file uploaded"

if __name__ == "__main__":
    app.run(debug=True)