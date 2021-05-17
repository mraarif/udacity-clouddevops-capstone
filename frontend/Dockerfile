FROM node:14-alpine

WORKDIR /usr/src/frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/frontend/node_modules/.bin:$PATH
ARG BACKEND_IP
ENV REACT_APP_BACKEND_IP $BACKEND_IP

COPY headliner/package.json ./
COPY headliner/package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY headliner/ ./

RUN npm run build && npm install -g serve
CMD serve -s build/
