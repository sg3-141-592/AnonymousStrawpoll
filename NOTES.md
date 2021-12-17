```
docker build -t web-server .
docker run --name web-server -d -p 80:80 web-server

docker build -t app-server .
docker run --name app-server -d -p 8000:8000 app-server

docker compose build --force-rm
docker compose up
```

```
artillery run -o results.json performance.yaml
artillery report results.json
```