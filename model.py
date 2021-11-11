import os.path

from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

IMAGES_ID = 0
model = load_model("model")


def preprocess_image(img):
    """Resize img to 28x28 and normalize for model input."""
    img = Image.open(img)
    img = img.resize((28, 28))
    np_img = np.asarray(img)[:, :, 3]
    return np_img / 256


def save_img_file(img):
    """Save img to images directory."""
    global IMAGES_ID
    img = preprocess_image(img)
    img_path = os.path.abspath(os.path.join("./images", f"img_{IMAGES_ID}"))
    IMAGES_ID += 1
    np.save(img_path, img)
    return img_path


def predict_num(num_img):
    """Predicting a number from img."""
    img = preprocess_image(num_img)
    # np.save('img_example', img)
    model_output = model.predict(np.expand_dims(img, axis=0))
    predicted_num = np.argmax(model_output)
    return predicted_num
