from flask import Flask, render_template, request
from model import predict_num

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        img = request.files["img"]
        num = predict_num(img)

        return {
            "num": str(num)
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
