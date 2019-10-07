# demo-flask-mongodb

Demo of a restful API based on flask + flask-restplus + mongoengine + mongodb

- Start the stack
```
docker-compose up -d --build
``` 

- Tell me the existing routes
```
docker-compose run --rm app flask routes
``` 

- Populate with some data
``` 
docker-compose run --rm app flask populate
``` 
