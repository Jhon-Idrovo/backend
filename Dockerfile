FROM python:3.9.2-slim

RUN echo "Building backend image"

WORKDIR /usr/local/app

# We copy the requirements first to avoid invalidating the cached packages
COPY ./requirements.txt /usr/local/app/
RUN pip install -r requirements.txt

# Copy the rest of the source code
COPY ./ ./
 

EXPOSE 8000

ENV IS_DEV="TRUE"

# Used to enable logs
ENV PYTHONUNBUFFERED=1

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# RUN python manage.py migrate
# To run this, the database needs to be online
CMD [ "python", "manage.py", "migrate" ]