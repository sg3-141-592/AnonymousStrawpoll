```
docker build -t web-server .
docker run --name web-server -d -p 8080:80 web-server
```