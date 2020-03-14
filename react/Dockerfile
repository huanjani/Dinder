FROM node:current

WORKDIR /app

COPY . /app
RUN npm install

EXPOSE 3000
CMD ["npm", "build"]
# changed from "npm", "start" to make faster