from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from model import predict_num

app = Flask(__name__)

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://neo:1234@mnist_problem-db-1:5432/imagesdb')
Base.metadata.create_all(engine)
IMAGES_ID = 0


class Images(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    line_width = Column(Integer)
    number = Column(Integer)
    number_image = Column(BLOB)


images = Images()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        img = request.files["img"]
        num = str(predict_num(img))
        return dict(num=num)


@app.route("/save-img", methods=['POST'])
def save_img():
    if request.method == 'POST':
        ins = images.id
        print(ins)
        return {}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
