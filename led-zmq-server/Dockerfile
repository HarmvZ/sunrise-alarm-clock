FROM python:3.7.4-buster as base-stage
COPY requirements /home/docker/requirements/
RUN pip3 install -r /home/docker/requirements/requirements.txt

# set timezone
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY . /home/docker/code/

# RUN pip3 install https://github.com/ismailof/mopidy-json-client/archive/master.zip TODO change when PR is accepted
RUN pip3 install https://github.com/HarmvZ/mopidy-json-client/archive/master.zip

FROM base-stage as develop-stage
RUN pip3 install -r /home/docker/requirements/local.txt
CMD ["python", "/home/docker/code/app/zmq_server.py"]


FROM base-stage as production-stage
RUN pip3 install -r /home/docker/requirements/production.txt
CMD ["python", "/home/docker/code/app/zmq_server.py"]
