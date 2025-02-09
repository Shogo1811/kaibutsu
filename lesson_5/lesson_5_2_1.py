from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, world!"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/user/<username>")
def user(username):
    return f"Hello, {username}!"

def user(username):
    return f"Hello, {username}!"

# HTTPメソッドの使い分け
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "Form submitted!"
    return "Send a POST request to submit."

if __name__ == "__main__":
    app.run(debug=True, port=5001)
