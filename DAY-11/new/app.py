from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = r"C:\Users\91906\OneDrive\Desktop\primary track capg\DAY-11\new\static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure the folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("uploads.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file and file.filename:
        # Save file into static/uploads
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Build URL for the uploaded file
        image_url = url_for("static", filename= file.filename)

        # Render template to display image
        return render_template("display.html", image_url=image_url)

    return "No file uploaded"

if __name__ == "__main__":
    app.run(debug=True)