from flask import Flask, request, send_file
import os
from detector import detect_mask

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files:
        return {"error": "No file part"}, 400

    file = request.files["image"]
    if file.filename == "":
        return {"error": "No selected file"}, 400

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(UPLOAD_FOLDER, "output_" + file.filename)
    file.save(input_path)
    detect_mask(input_path, output_path)
    return send_file(output_path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)
