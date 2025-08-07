import time

from celery import Celery
from logger import log


REDIS_HOST = "10.168.171.198"
REDIS_PORT = "8083"
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"


celery_app = Celery("celery_app", broker=REDIS_URL, backend=REDIS_URL)


@celery_app.task(acks_late=True, reject_on_worker_lost=True)
def continue_task(name: str) -> None:
    for i in range(10):
        log.info(f"Hello {name}, the time is {time.time()}")
        time.sleep(2)
