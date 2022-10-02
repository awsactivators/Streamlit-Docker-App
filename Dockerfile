FROM python:3.8

ENV STREAM_APP=/home/app/webapp

# set work directory
RUN mkdir -p $STREAM_APP

# where your code lives
WORKDIR $STREAM_APP

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy project
COPY . $STREAM_APP

RUN pip install -r requirements.txt

EXPOSE 8501
docker ps

CMD streamlit run app.py