FROM python:3.11
COPY ./requirements.txt /build/requirements.txt
WORKDIR /build
RUN pip --no-cache-dir install --requirement requirements.txt
COPY . /build
ENV FLASK_RUN_HOST="0.0.0.0"
ENV FLASK_RUN_PORT=8080
CMD ["flask", "run"]
