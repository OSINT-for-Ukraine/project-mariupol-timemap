FROM node:20-alpine
WORKDIR /app
COPY package.json ./package.json
COPY package-lock.json ./package-lock.json
COPY --chown=node:node . /app
RUN npm install
RUN npm run build
EXPOSE 8080
USER node
CMD [ "npm", "run", "serve"]