FROM python:3.6-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
#COPY src/requirements.txt ./

RUN cd /app && \
    git clone https://github.com/navodissa/tinyurl.git && \
    cd tinyurl && pip3 install -r requirements.txt && \
    cd backend/write

# Bundle app source
#COPY src /app

EXPOSE 8080
CMD [ "python3", "/app/tinyurl/backend/write/app.py" ]
