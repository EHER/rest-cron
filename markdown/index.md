#REST Cron
A REST way to manage your Cron

List schedulled jobs:

```
curl -XGET http://localhost:8080/cron
```


Get a job with id 1:

```
curl -XGET http://localhost:8080/cron/1
```


Delete a job with id 2:

```
curl -XDELETE http://localhost:8080/cron/2
```

