### Create virutal environment
- ```python3 -m venv ENV_NAME```
- ```source ENV_NAME/bin/activate```

### Install FastAPI library
- ```pip install fastapi[standard]```

- Run: ```fastapi run```
- Run (auto-reload): ```fastapi run --reload```
- Run from specific file: ```fastapi run main.py```
- Run with host & port: ```fastapi run --host localhost --port 8000```

OR 
- Run: ```uvicorn main:app --reload```

### Application serving
- Browser JSON format: ```http://localhost:8000```
- Swagger UI: ```http://localhost:8000/docs```
- Redocly UI: ```http://localhost:8000/redoc```

### For tests
- ```pip install pytest```

- Run:
`pytest`
