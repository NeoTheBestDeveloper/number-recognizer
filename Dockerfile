FROM tensorflow/tensorflow 

RUN mkdir /usr/src/app

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "server.py"]
