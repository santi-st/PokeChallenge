# <b>PokeChallenge </b>

This is the repository for the PokeChallenge app.


## Deploy

### Runing with Docker in your local

- Download Docker and Docker Compose
- Clone the repo
- Run in the terminal (inside the repo dir):
```console
docker build -t pokeapi .
```
- Once the image have been built, run in the terminal:
```console
docker run -d --name mycontainer -p 80:80 pokeapi
```
- Now the API is running at http://127.0.0.1/ &ensp; (localhost)

### Manual deploy 

- Clone the repo
- Run in terminal, on the requirements.txt dir:
```console
run: pip install -r requirements.txt
```
- Once the requirements have been install, run in terminal in app dir:
```console
uvicorn main:app --reload
```
- In the next message we get the url to start using the api
```console
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [19008] using statreload
INFO:     Started server process [6372]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Examples
- GET /{nombreDelPokemon}
```console
http://127.0.0.1/growlithe
```
- GET / -> Listado de pokemons
```console
http://127.0.0.1/?q=cha&offset=1&limit=5
```

### Endpoint Documentation
- Acces the Endpoint interactive documentation:
- Swagger UI
```console
http://127.0.0.1/docs
```
- ReDoc
```console
http://127.0.0.1/redoc
```

### Testing
- Run in terminal:
```
pytest -vv
```
