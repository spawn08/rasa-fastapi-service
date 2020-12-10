FROM python:3.7.4

RUN apt-get update
RUN apt-get -y  upgrade
WORKDIR /ml_app
COPY . /ml_app

RUN pip --no-cache-dir install rasa
RUN pip --no-cache-dir install uvicorn
RUN pip --no-cache-dir install fastapi
EXPOSE 3456
CMD ["python3", "run.py"]