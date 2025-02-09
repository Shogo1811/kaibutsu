from flask import Flask, jsonify, request

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

# HTTPメソッドの使い分け
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "Form submitted!"
    return "Send a POST request to submit."


@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("name")  # フォームデータ
    age = request.form.get("age") #追加データ
    if not name:
        return "Name is required!", 400
    if not age or not age.isdigit() or int(age) <= 0:
        return "Valid age is required!", 400
    return f"Form submitted successfully! Hello, {name}!, You are {age} years old."


@app.route("/api/data", methods=["POST"])
def api_data():
    print("test")
    print(request.get_json())
    data = request.get_json()  # JSONデータ
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"message": f"Hello, {data['name']}!"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
