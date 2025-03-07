FROM python:3.9.2

WORKDIR /usr/local/app

# Copy source code
COPY ./ ./

# Install the application's dependencies 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENV IS_DEV "TRUE"
ENV PYTHONUNBUFFERED 1
# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# To run this, the database needs to be online
# RUN python manage.py migrate
# CMD [ "python", "manage.py", "migrate" ]
# CMD [ "python", "manage.py", "runserver" ]
# CMD ["gunicorn","main_app.wsgi","--log-file","-"]