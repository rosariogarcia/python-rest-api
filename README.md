# python-rest-api
Most easy Python rest API with Flask in order to create an image with Dockerfile

#Steps to create the image:

1. Clone the repository
2. Build the image with dockerfile running command:
    docker build -t myapp:1.0 .
3. Run the container with command:
    docker run -d --restart always --name myapp -p 4000 myapp:1.0
