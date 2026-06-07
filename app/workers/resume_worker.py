from rq import Worker
from rq import Queue

from app.core.redis import redis_client

queues = [
    Queue(
        "resume-processing",
        connection=redis_client
    )
]

worker = Worker(
    queues,
    connection=redis_client
)

worker.work()