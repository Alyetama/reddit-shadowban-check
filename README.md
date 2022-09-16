# Reddit Shadowban Check

Web app to check whether a user is shadowbanned from Reddit.


```shell
git clone https://github.com/Alyetama/reddit-shadowban-check.git
cd reddit-shadowban-check
```

```shell
docker run \
  -d --restart unless-stopped \
  -p 8501:8501 \
  alyetama/reddit-shadowban-check:latest
```
