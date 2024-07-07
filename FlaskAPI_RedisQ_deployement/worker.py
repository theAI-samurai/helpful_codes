import redis
from rq import Worker, Queue, Connection

listen = ['default']

conn = redis.Redis()

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()

# start flask application
# python app.py
# Start the RQ worker:
# python worker.py
