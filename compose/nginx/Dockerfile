FROM node:13-alpine AS builder

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# set working directory
WORKDIR /app

# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY ./frontend/package*.json  /app/
RUN npm install --silant

COPY ./frontend /app/

RUN ng build --prod

# Stage - 2
FROM nginx:1-alpine

RUN rm -rf /usr/share/nginx/html/*

COPY --from=builder /app/dist/frontend/ /usr/share/nginx/html