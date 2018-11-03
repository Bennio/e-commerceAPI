FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev build-essential
COPY e-commerceAPI /app
WORKDIR /app
RUN pip3 install -r requirements.txt && \
python3 -m install python-psycopg2
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["run.py"]