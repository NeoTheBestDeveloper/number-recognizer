from flask import Flask, render_template, request, send_file
from database.images.image import *
from database.base import Session, engine, Base
from model import predict_num

app = Flask(__name__)

# Generate database schema
Base.metadata.create_all(engine)

# Create a new session
session = Session()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        img = request.files["img"]
        num = str(predict_num(img))
        return dict(num=num)


@app.route("/save-image", methods=['POST'])
def save_image():
    if request.method == 'POST':
        # Get data from request
        data = request.form
        line_width = int(data["line_width"])
        right_number = int(data["right_number"])
        image = request.files["img"]

        # Create image service instance and saving image with same metadata
        image_service = ImageService()
        image_service.insert_image(image, line_width, right_number)

        return {
            "payload": "ok"
        }


@app.route("/get-images", methods=['GET'])
def get_images():
    dataset_path = ImageRepository.get_images()

    return send_file(dataset_path, "dataset.npz")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
