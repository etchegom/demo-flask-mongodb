# demo-flask-mongodb

Demo of a restful API based on flask + flask-restplus + mongoengine + mongodb

- Start the stack
```
docker-compose up -d --build
``` 

- Populate with some data
(you need an [OMDB api key](https://www.omdbapi.com/apikey.aspx))
``` 
docker-compose run --rm app flask populate --reset --apikey=<your_api_key> --search=starwars --type=movie
``` 

- Tell me the existing routes
```
docker-compose run --rm app flask routes
``` 

- Get a list of movies using [httpie](https://httpie.org/) for instance
```
http --follow http://localhost:5000/api/movies/
```