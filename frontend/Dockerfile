FROM nginx:latest
COPY dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY fullchain.pem /etc/nginx/fullchain.pem
COPY privkey.pem /etc/nginx/privkey.pem
EXPOSE 443
EXPOSE 80