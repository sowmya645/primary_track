from flask import Flask, render_template, request
from models import db, User

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()
    # Add a sample user if not exists
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", password="1234")
        db.session.add(admin)
        db.session.commit()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return f"Welcome, {username}!"
    else:
        return "Invalid credentials. Try again."

if __name__ == "__main__":
    app.run(debug=True)