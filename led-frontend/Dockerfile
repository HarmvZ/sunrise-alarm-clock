# develop stage
FROM node:14.13.1-alpine3.10 as develop-stage
WORKDIR /app
COPY package*.json ./
RUN yarn global add @quasar/cli
COPY . .
# build stage
FROM develop-stage as build-stage
ARG HOSTNAME
ARG WLED_WS
ARG WLED_UI
ARG WLED_API
ARG MOPIDY_WS
ARG MOPIDY_UI
ARG MOPIDY_API
RUN yarn
RUN quasar build
RUN echo $WLED_API
# production stage
FROM nginx:1.19.7-alpine as production-stage
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
