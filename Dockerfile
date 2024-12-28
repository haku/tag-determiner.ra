# https://hub.docker.com/_/python/
FROM python:3.10-bookworm

WORKDIR /usr/src/app

RUN git clone https://github.com/xinyu1205/recognize-anything.git
RUN pip install -e recognize-anything/

COPY requirements.txt *.py *.pyi *.proto ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 30033
ENTRYPOINT ["/usr/src/app/ram-td.py"]
