FROM node:lastest AS build

WORKDIR /usr/src/app

COPY . .

RUN npm install --production
RUN npm run build

