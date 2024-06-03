FROM tiangolo/uwsgi-nginx:python3.8-alpine

RUN apk update && \
    apk add --no-cache \
        bash \
        chromium \
        chromium-chromedriver \
        nss \
        freetype \
        harfbuzz \
        ttf-freefont \
        font-noto

ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/


COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./Templates/* /app/Templates/
COPY ./tests/* /app/tests/
COPY requirements.txt /tmp/


RUN pip install --requirement /tmp/requirements.txt


EXPOSE 8777


CMD ["python", "/app/MainScores.py"]
