from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq_aio_pika import AioPikaBroker

from services import handler

broker = AioPikaBroker("amqp://guest:guest@rmq:5672/")


scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


@broker.task(schedule=[{"cron": "*/5 * * * *"}])
async def get_pandora_data():
    # await handler.update_audiences()
    await handler.get_last_records()
    await handler.check_incidents()

