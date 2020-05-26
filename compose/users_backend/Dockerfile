FROM python:3.7-alpine

LABEL maintainer="Devansh Kumar <devansh2290@gmail.com>"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
  # mysql dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add mariadb-dev \
    # CFFI dependencies
  && apk add libffi-dev py-cffi

# Requirements are installed here to ensure they will be cached.
COPY ./users_backend/requirements /requirements
RUN pip install -r /requirements/local.txt \
    && rm -rf /requirements

COPY ./compose/users_backend/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/users_backend/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./users_backend/src/app /app

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

EXPOSE 5000