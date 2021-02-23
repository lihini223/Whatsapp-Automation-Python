from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from honey_love import send_message

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_message, 'interval', seconds=10)

sched.start()
