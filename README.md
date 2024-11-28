# Simple Storage API

This is a simple Flask API that can store and retrieve data.

## Endpoints

- `POST /api/data`: Store new data
- `GET /api/data`: Retrieve the latest stored data

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The server will start at `http://localhost:5000`

## Example Usage

### Store Data (POST)
```bash
curl -X POST -H "Content-Type: application/json" -d '{"message":"Hello World"}' http://localhost:5000/api/data
```

### Retrieve Data (GET)
```bash
curl http://localhost:5000/api/data
```
