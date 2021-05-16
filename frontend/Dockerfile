FROM node:14-alpine

WORKDIR /usr/src/frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/frontend/node_modules/.bin:$PATH

COPY headliner/package.json ./
COPY headliner/package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

COPY headliner/ ./

ARG BACKEND_IP

ENV BACKEND_IP $BACKEND_IP


CMD cd headliner && npm start
