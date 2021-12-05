```
docker build -t web-server .
docker run --name web-server -d -p 8080:80 web-server

docker build -t app-server .
docker run --name app-server -d -p 8080:80 app-server
```