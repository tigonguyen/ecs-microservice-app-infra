FROM python:3.10-slim-bullseye
COPY . /
WORKDIR /
RUN pip install flask
EXPOSE 8001
ENTRYPOINT ["python"]
CMD ["app.py"]
