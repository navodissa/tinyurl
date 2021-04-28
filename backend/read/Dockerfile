FROM python:3.6

# Create app directory
WORKDIR /app

# Install app dependencies
#COPY src/requirements.txt ./

RUN cd /app
RUN git clone https://github.com/navodissa/tinyurl.git
RUN cd /app/tinyurl/backend/read

# Bundle app source
#COPY src /app

EXPOSE 8081
CMD [ "python3", "/app/tinyurl/backend/read/app.py" ]
