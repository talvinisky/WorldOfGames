##FROM tiangolo/uwsgi-nginx:python3.8-alpine
##
### Install necessary dependencies
##RUN apk update && \
##    apk add --no-cache \
##        bash \
##        chromium \
##        chromium-chromedriver \
##        nss \
##        freetype \
##        harfbuzz \
##        ttf-freefont \
##        font-noto
##
### Set environment variables
##ENV CHROME_BIN=/usr/bin/chromium-browser \
##    CHROME_PATH=/usr/lib/chromium/
##
### Copy application files
##COPY ./Scores.txt /app/
##COPY ./*.py /app/
##COPY ./Templates/* /app/Templates/
##COPY ./tests/* /app/tests/
##COPY requirements.txt /tmp/
##
### Install Python dependencies
##RUN pip install --requirement /tmp/requirements.txt
##
### Expose the application port
##EXPOSE 8777
##
### Start the application
##CMD ["python", "/app/MainScores.py"]
#FROM tiangolo/uwsgi-nginx:python3.8-alpine
#
## Install necessary dependencies
#RUN apk update && \
#    apk add --no-cache \
#        bash \
#        chromium \
#        chromium-chromedriver \
#        nss \
#        freetype \
#        harfbuzz \
#        ttf-freefont \
#        font-noto \
#        dbus \
#        ttf-dejavu
#
## Set environment variables
#ENV CHROME_BIN=/usr/bin/chromium-browser \
#    CHROME_PATH=/usr/lib/chromium/
#
## Copy application files
#COPY ./Scores.txt /app/
#COPY ./*.py /app/
#COPY ./Templates/* /app/Templates/
#COPY ./tests/* /app/tests/
#COPY requirements.txt /tmp/
#
## Install Python dependencies
#RUN pip install --requirement /tmp/requirements.txt
#
## Expose the application port
#EXPOSE 8777
#
## Start the application
#CMD ["python", "/app/MainScores.py"]
FROM tiangolo/uwsgi-nginx:python3.8-alpine

# Install necessary dependencies
RUN apk update && \
    apk add --no-cache \
        bash \
        chromium \
        chromium-chromedriver \
        nss \
        freetype \
        harfbuzz \
        ttf-freefont \
        font-noto \
        dbus \
        ttf-dejavu

# Set environment variables
ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/

# Copy application files
COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./Templates/* /app/Templates/
COPY ./tests/* /app/tests/
COPY requirements.txt /tmp/

# Install Python dependencies
RUN pip install --requirement /tmp/requirements.txt

# Expose the application port
EXPOSE 8777

# Start the application
CMD ["python", "/app/MainScores.py"]
