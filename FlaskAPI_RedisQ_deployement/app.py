from flask import Flask, request, jsonify
import redis
from rq import Queue
from rq.job import Job
from worker import conn
from multiply import multiply

app = Flask(__name__)

# Redis connection and Queue setup
redis_conn = redis.Redis()
q = Queue(connection=redis_conn)

# Function to be executed in the background


@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    try:
        data = request.get_json()
        x = data['x']
        y = data['y']

        # Queue the task
        job = q.enqueue(multiply, x, y)

        response = {
            "job_id": job.get_id(),
            "status": "Job enqueued"
        }
        return jsonify(response), 202

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/result/<job_id>', methods=['GET'])
def get_result(job_id):
    try:
        job = Job.fetch(job_id, connection=redis_conn)

        if job.is_finished:
            response = {
                "result": job.result
            }
        else:
            response = {
                "status": "Job still processing"
            }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)