**TODO**:
- Make the database path configurable at runtime
   - Provide a Sqlite mount onto Azure storage
- Provide a SQL database
- Provide a health endpoint for the app
- Provide an Azure Pipeline to build the Container image
- Provide an Azure Release Pipeline to update the App
```
docker build -t web-server .
docker run --name web-server -d -p 80:80 web-server

docker build -t app-server .
docker run --name app-server -d -p 8000:8000 app-server

docker-compose build --force-rm
docker-compose up

docker logs 9826 > NginxLogs.txt
sudo goaccess NginxLogs.txt -o nginx.html --log-format=COMBINED
python3 -m http.server

sqlite3 /var/lib/docker/volumes/anonymousstrawpoll_databasevol/_data/data.db

# Number of polls created by user
select userId, count(userId) from polls
group by userId;

# Get number of users who have voted in each poll
select pollId, count(distinct userId) from votes
group by pollId;

# Get number of votes on each poll
select pollId, count(userId) from votes
group by pollId;
```

```
artillery run -o results.json performance.yaml
artillery report results.json
```

```
Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
docker tag anonymousstrawpoll_backend livepollregistry.azurecr.io/livepoll/backend
docker tag anonymousstrawpoll_frontend livepollregistry.azurecr.io/livepoll/frontend
docker push livepollregistry.azurecr.io/livepoll/backend
docker push livepollregistry.azurecr.io/livepoll/frontend
```