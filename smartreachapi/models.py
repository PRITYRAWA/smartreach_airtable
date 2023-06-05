from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Prospects(models.Model):
    class categorychoices(models.TextChoices):
        CONVERTED = 'Converted'
        INTERESTED = 'Interested'
        NOT_INTERESTED = 'Not Interested'
        NOT_NOW = 'Not now'
        AUTO_REPLY = 'Auto reply'
        DELIVERY_FAILED = 'Delivery failed'
        DO_NOT_CONTACT = 'Do not contact'
        NOT_CATEGORIZED = 'Not categorized'
        OUT_OF_OFFICE = 'Out of office'
    prospect_id = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=False, null=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100,choices=categorychoices.choices, default=categorychoices.NOT_CATEGORIZED)
    owner = models.IntegerField(blank=True, null=True)
    team = models.IntegerField(blank=True, null=True)
    list = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    time_zone = models.CharField(max_length=100, null=True, blank=True)
    added_on = models.DateTimeField(null=True, blank=True)
    last_contacted_at = models.DateTimeField(null=True, blank=True)
    latest_reply_sentiment_uuid = models.IntegerField(null=True, blank=True)
    current_step_type = models.CharField(max_length=100, null=True, blank=True)
    latest_task_done_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [
            ['prospect_id', 'email','first_name', 'last_name','category','owner','team', 'list', 'company', 'city', 
                           'state', 'phone', 'job_title', 'linkedin_url', 'country', 'time_zone', 'added_on', 'last_contacted_at',
                          'latest_reply_sentiment_uuid',  'current_step_type', 'latest_task_done_at', 'created_at']
        ]



