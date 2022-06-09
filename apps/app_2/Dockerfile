FROM python:3.10-slim-bullseye

COPY . /
WORKDIR /

ARG APP_1_HOST=localhost
ENV APP_1_HOST=$APP_1_HOST


RUN pip install flask requests
EXPOSE 8002
ENTRYPOINT ["python"]
CMD ["app.py"]
