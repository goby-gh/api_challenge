FROM python:3.8-slim-buster
ARG DIR=/app

# set work directory
WORKDIR $DIR

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# install build dependencies
RUN apt-get update && apt-get -y install g++ libpq-dev gcc unixodbc unixodbc-dev
RUN pip install --upgrade pip

# install project reqs
# COPY ./requirements.txt ${DIR}/requirements.txt
# RUN pip install -r requirements.txt

# copy project
COPY . $DIR

# ENTRYPOINT ["/app/wait-for-it.sh", "db:5432", "--"]
CMD ["python", "challenge.py"]
