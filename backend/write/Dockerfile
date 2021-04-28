FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
#COPY src/requirements.txt ./

RUN cd /app
RUN git clone https://github.com/navodissa/tinyurl.git
RUN cd /app/tinyurl/backend/write

# Bundle app source
#COPY src /app

EXPOSE 8080
CMD [ "python3", "/app/tinyurl/backend/write/app.py" ]
