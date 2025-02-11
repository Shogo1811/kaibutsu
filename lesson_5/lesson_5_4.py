from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("name")  # フォームデータ
    age = request.form.get("age") #追加データ
    if not name:
        return "Name is required!", 400
    if not age or not age.isdigit() or int(age) <= 0:
        return "Valid age is required!", 400
    return f"Form submitted successfully! Hello, {name}!, You are {age} years old."

if __name__ == "__main__":
    app.run(debug=True, port=5001)
