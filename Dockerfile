FROM tiangolo/uwsgi-nginx:python3.8-alpine

COPY ./Scores.txt /app/
COPY ./*.py /app/
COPY ./Templates/* /app/Templates/
COPY ./tests/* /app/tests/
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

EXPOSE 8777
CMD ["python", "/app/MainScores.py"]

