from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from model import predict_num, save_img_file

app = Flask(__name__)

Base = declarative_base()
engine = create_engine('postgresql+psycopg2://neo:1234@mnist_problem-db-1:5432/imagesdb', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class Images(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    line_width = Column(Integer)
    num = Column(Integer)
    num_image = Column(String)


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


@app.route("/save-image", methods=['POST'])
def save_image():
    if request.method == 'POST':
        data = request.form
        line_width = data["line_width"]
        right_number = data["right_number"]
        image = request.files["img"]
        image_path = save_img_file(image)

        i = Images(line_width=line_width, num=right_number, num_image=image_path)
        session = Session()
        session.add(i)
        session.commit()
        session.close()

        return {
            "payload": "ok"
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
