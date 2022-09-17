FROM node:alpine
WORKDIR /web
COPY ./package.json ./package-lock.json /web/
RUN npm install
COPY . /web/
CMD [ "npm", "run", "dev" ]