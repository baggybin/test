from flask import Flask, request, jsonify, abort
import random
import string
import requests

app = Flask(__name__)
def random_letters(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

@app.route("/upload", methods=["POST"])
def upload():
    file_obj = request.files.get("file")
    if not file_obj:
        abort(400, description="No file provided")
    return jsonify({"filename": file_obj.filename, "size": file_obj.content_length}), 201

@app.route("/", methods=["GET"])
def root():
    n = random.randint(10, 50)  # integer length between 10 and 50
    body = f"Hello from C2 Server: {random_letters(n)}\n"
    return body, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route("/", methods=["POST"])
def count_bytes():
    raw = request.get_data()        
    size = len(raw)
    return {"byte_count": size}, 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)