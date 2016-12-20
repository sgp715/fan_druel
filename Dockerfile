FROM ubuntu:14.04


RUN apt-get -y update


RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN apt-get install -y python-pip
RUN apt-get install -y sqlite3


COPY . /src/
WORKDIR /src/
RUN pip install -r requirements.txt


RUN npm install -g webpack
WORKDIR /src/app/
RUN npm install
RUN webpack


# initialize database


WORKDIR /src/
EXPOSE 8080
CMD ["python", "server.py"]
