FROM python:3.7-alpine

LABEL maintainer="Devansh Kumar <devansh2290@gmail.com>"

ARG BUILD_ENV=production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
  # mysql dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add mariadb-dev

# Requirements are installed here to ensure they will be cached.
COPY ./todos_backend/requirements /requirements
RUN pip install -r /requirements/${BUILD_ENV}.txt \
    && rm -rf /requirements

COPY ./compose/todos_backend/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/todos_backend/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./todos_backend/src/app /app

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

EXPOSE 5001