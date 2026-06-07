## Commands

- Create and activate a virtual environment

```sh
python -m venv .venv
source .venv/bin/activate
```

- Install dependencies

```sh
pip install -r requirements.txt
```

- Run server

```sh
uvicorn app.main:app --reload
```

- [Open Swagger UI](http://127.0.0.1:8000/docs)

```sh
http://127.0.0.1:8000/docs
```

- [Open ReDoc](http://127.0.0.1:8000/redoc)

```sh
http://127.0.0.1:8000/redoc
```