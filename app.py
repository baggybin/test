from flask import Flask

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file_obj = request.files.get("file")
    if not file_obj:
        abort(400, description="No file provided")
    return jsonify({"filename": file_obj.filename, "size": file_obj.content_length}), 201

@app.route("/", methods=["GET"])
def root():
    return "Hello from Cloud Run!"

@app.route("/", methods=["POST"])
def echo():
    if not request.is_json:
        abort(400, description="Content-Type must be application/json")
    data = request.get_json(silent=True)
    if data is None:
        abort(400, description="Invalid JSON")
    return jsonify({"received": data}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)