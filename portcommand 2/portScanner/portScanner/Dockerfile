FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y make \
     && apt-get clean \
     && rm -rf /var/lib/apt/lists/*

RUN make install

ENTRYPOINT ["python"]
CMD ["main.py", "--help"]

