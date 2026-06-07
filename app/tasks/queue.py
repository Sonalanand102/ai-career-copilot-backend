from rq import Queue

from app.core.redis import redis_client

resume_queue = Queue(
    "resume-processing",
    connection=redis_client
)