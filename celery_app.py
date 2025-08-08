import time

from celery import Celery
from logger import log

RMQ_USER = "user"
RMQ_PASSWORD = "password"
RMQ_HOST = "10.168.171.198"
RMQ_PORT = "8083"
REDIS_URL = f"amqp://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_HOST}:{RMQ_PORT}//"


celery_app = Celery("celery_app", broker=REDIS_URL, backend="rpc://")


@celery_app.task(
    bind=True,
    acks_late=True,
    reject_on_worker_lost=True,
    max_retries=3,
    default_retry_delay=5,
    # autoretry_for=(Exception,),
)
def continue_task(self, name: str) -> None:
    for i in range(10):
        log.info(f"Hello {name}, the time is {time.time()}")
        time.sleep(2)
