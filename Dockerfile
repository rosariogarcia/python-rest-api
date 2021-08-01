FROM python:3-alpine3.8

RUN pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD [ "python3", "src/app.py"]