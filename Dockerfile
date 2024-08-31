# https://hub.docker.com/_/python/
FROM python:3.10-bookworm

WORKDIR /usr/src/app
COPY requirements.txt *.py *.pyi *.proto ./
COPY ram_plus_swin_large_14m.pth ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/xinyu1205/recognize-anything.git
RUN pip install -e recognize-anything/

EXPOSE 30033
ENTRYPOINT ["/usr/src/app/ram-td.py"]
