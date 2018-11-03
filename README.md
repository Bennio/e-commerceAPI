
## e-commerceAPIS
Basic CRUD e-commerse REST API 

## Building the Docker Container

```
$ docker build -f Dockerfile -t $DOCKER_USER_ID/run-api-logic .
```

## Running the Docker Container

```
$ docker run -d -p 5050:5000 $DOCKER_USER_ID/run-api-logic
```

The app is listening by default on port 5000. The 5050 port of the host machine is mapped to the port 5000 of the container.

-p 5050:5000 i.e.

``` -p <hostPort>:<containerPort>```

### Verifying that it works

Execute a POST on endpoint 

-> `localhost:5050/api/ecommerce` or 

-> `<docker-machine ip>:5050/analyse/sentiment` Docker-machine ip has to be used if your OS doesn't provide native docker support. 

Request body:

```
{
    "sentence": "I hate you!"
}
```

## Pushing to Docker Hub

```
$ docker push $DOCKER_USER_ID/run-api-logic
```