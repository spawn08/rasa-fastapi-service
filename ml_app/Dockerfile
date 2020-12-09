FROM python:3.6

RUN apt-get update
RUN apt-get -y  upgrade
WORKDIR /ml_app
COPY . /ml_app

RUN pip install rasa
RUN pip install uvicorn
RUN pip install fastapi
EXPOSE 3456
CMD ["python3", "run.py"]