# https://hub.docker.com/_/python/
FROM python:3.10-bookworm

WORKDIR /usr/src/app

RUN pip install git+https://github.com/xinyu1205/recognize-anything.git

COPY requirements.txt *.py *.pyi *.proto ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 30033
ENTRYPOINT ["/usr/src/app/ram-td.py"]
