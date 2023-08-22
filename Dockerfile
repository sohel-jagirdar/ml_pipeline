FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
<<<<<<< HEAD
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app  # Web Server Program
=======
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
>>>>>>> 99cc3f5da480626cb982475c5c2d16c8952c1104





