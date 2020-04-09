FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE=1

RUN python -m pip install --upgrade pip

WORKDIR /app

COPY dev-requirements.txt .
RUN pip3 install -r dev-requirements.txt

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /app
RUN pip3 install -e .