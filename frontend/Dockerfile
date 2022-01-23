FROM node:16 as build-stage
ADD ./  $HOME/frontend/
WORKDIR $HOME/frontend/
RUN npm install
RUN npm run build

FROM nginx:latest as production-stage
COPY --from=build-stage $HOME/frontend/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 443
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]