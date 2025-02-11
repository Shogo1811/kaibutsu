from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")  # クエリパラメータ
    return f"Hello, {name}!"

@app.route("/custom", methods=["GET"])
def custom_response():
    return "This is a custom response!", 202

@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("name")  # フォームデータ
    if not name:
        return "Name is required!", 400
    return f"Form submitted successfully! Hello, {name}!"

@app.route("/api/data", methods=["POST"])
def api_data():
    data = request.get_json()  # JSONデータ
    if not data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400
    return jsonify({"message": f"Hello, {data['name']}!"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
