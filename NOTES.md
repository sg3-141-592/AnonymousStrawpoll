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
Migration
sqlite3 database/data.db < migrations/01-addPollTypeColumn.sql
```

```
artillery run -o results.json performance.yaml
artillery report results.json
```