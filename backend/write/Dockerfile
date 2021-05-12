FROM python:3.6-slim-buster

# Create app directory
WORKDIR /app

# Install app dependencies
#COPY src/requirements.txt ./

RUN cd /app && \
#<<<<<<< HEAD
    apt-get update && \
    apt-get install git -y && \
#=======
    apt-get install git && \
#>>>>>>> b660cc62c03b8b950cca7777cc2368382095fe02
    git clone https://github.com/navodissa/tinyurl.git && \
    cd tinyurl && pip3 install -r requirments.txt && \
    cd backend/write

# Bundle app source
#COPY src /app

EXPOSE 8080
EXPOSE 8081
CMD [ "sh", "/app/tinyurl/start_app.sh" ]
