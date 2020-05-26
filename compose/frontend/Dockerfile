FROM node:13-alpine AS alpine

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# set working directory
WORKDIR /app

# install angular-cli globally
RUN npm install -g @angular/cli

# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY ./frontend/package*.json  /app/
RUN npm install --silant

COPY ./frontend /app/

# start app
COPY ./compose/frontend/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start