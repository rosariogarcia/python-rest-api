FROM python:3-alpine3.8 as build

RUN pip3 install --upgrade pip
WORKDIR /tmp
COPY . /tmp
CMD [ "python3", "src/app.py"]

FROM python:3-alpine3.8
COPY --from=build . /app
EXPOSE 4000
CMD [ "python3", "src/app.py"]