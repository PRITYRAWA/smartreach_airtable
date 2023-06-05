from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import fetch_campaigns_data

def start():
    scheduler = BackgroundScheduler(job_defaults={'max_instances': 5})
    scheduler.add_job(fetch_campaigns_data, 'interval', minutes=30)
    scheduler.start()