FROM python:3.7.4-buster as base-stage
COPY requirements /home/docker/requirements/
RUN pip3 install -r /home/docker/requirements/requirements.txt
EXPOSE 5555
COPY . /home/docker/code/


FROM base-stage as develop-stage
RUN pip3 install -r /home/docker/requirements/local.txt
CMD ["python", "/home/docker/code/app/zmq_server.py"]


FROM base-stage as production-stage
RUN pip3 install -r /home/docker/requirements/production.txt
CMD ["python", "/home/docker/code/app/zmq_server.py"]
