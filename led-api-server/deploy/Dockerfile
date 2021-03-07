# Copyright 2013 Thatcher Peskens
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:20.04 as base-stage

# Install required packages and remove the apt packages cache when done.
RUN apt-get update && \
    apt-get upgrade -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nginx \
    supervisor \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    sqlite3 \
    curl && \
    pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH = "${PATH}:/root/.poetry/bin"

COPY pyproject.toml poetry.lock /home/docker/code/
WORKDIR /home/docker/code/

# Turn off virtualenv since the 
RUN poetry config virtualenvs.create false

FROM base-stage as develop-stage
RUN poetry install --no-ansi

COPY . /home/docker/code/


FROM base-stage as production-stage
# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY deploy/nginx-app.conf /etc/nginx/sites-available/default
COPY deploy/supervisor-app.conf /etc/supervisor/conf.d/

RUN poetry install --no-dev --no-ansi

COPY . /home/docker/code/

EXPOSE 8888
CMD ["supervisord", "-n"]
