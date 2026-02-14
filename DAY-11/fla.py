from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello,flask!"
if __name__=="__main__":
    app.run(debug=True)
@app.route("/about")
def about():
    return "this is about page"
@app.route("/user/<name>")
def user(name):
    return f"Hello,{name}"

if __name__=="__main__":
    app.run(debug=True)