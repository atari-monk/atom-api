## Record CRUD API Test

See [Commands](../../commands.md) to start server

### Swagger

Test using Swagger

### Curl

Test using curl in terminal

- Create record

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/model' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model_name": "test",
  "title": "test",
  "json_data": {
    "additionalProp1": "test"
  },
  "markdown_data": "# Title\n\n- item 1\n- item 2\n\n```python\nprint(\"hello\")\n```"
}'
```

- Get all records 

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/model' \
  -H 'accept: application/json'
```

- Get record by id

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/model/dd831d15-5144-4ee1-b7f3-eb01cf50f2ec' \
  -H 'accept: application/json'
```