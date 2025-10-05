FROM python:3.12-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/
EXPOSE 8000
#use 0.0.0.0 to make it accessible from outside the container
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]