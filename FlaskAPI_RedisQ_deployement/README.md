## This Illustrates deployment of a Flask API with Redis Queue on Linux System : helpful for handlig large incoming requests from API

```pip install Flask redis rq```

> **Multiply.py**  :  contains a Task Function example: multiplying 2 numbers. (This could be any task like an LLM/AI/Web Crawling ets).
> 
> **app.py**  : This is a Flask API + REDIS Queue code that calls the Task Function for Enqueing.
> 
> **worker.py** : This initiates the Redis Queue and makes sure all task functions in queue gets completed.

## Deployemt Steps
#### Start the Flask application
```python app.py```
#### Start the RQ worker
```python worker.py```


## sending post requesst and verifying
#### * *Enqueue a Task via a POST Request* *
```curl -X POST -H "Content-Type: application/json" -d '{"x": 2, "y": 3}' http://localhost:5000/multiply```

#### * *check on Result for a job id * *
```curl http://localhost:5000/result/<job_id>```

#### Flask API