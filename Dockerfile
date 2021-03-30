FROM python:3.8.5-buster
LABEL author="Richard Crouch"
LABEL description="Learning microservice"

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London

# Generate logs in unbuffered mode
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update
#RUN apt-get -y upgrade

# install Yoctopuce dependencies
#RUN apt-get -y install libusb-1.0.0 libusb-1.0.0-dev joe

# Install Python dependencies
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

# see value in definitions.py
EXPOSE 8081

# run Python unbuffered so the logs are flushed
CMD ["python3", "-u", "test_service.py"]
#CMD ["tail", "-f", "/dev/null"]
