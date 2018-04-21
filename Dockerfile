FROM python:2.7.14

ADD requirements.txt .
ADD dump_queue.py .

RUN mkdir -p /output && pip install -r requirements.txt

ENTRYPOINT ["python", "dump_queue.py"]
