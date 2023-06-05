# Generated by Django 4.1.7 on 2023-04-03 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartreachapi', '0008_alter_prospects_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prospects',
            unique_together={('prospect_id', 'email', 'first_name', 'last_name', 'category', 'owner', 'team', 'list', 'company', 'city', 'state', 'phone', 'job_title', 'linkedin_url', 'country', 'time_zone', 'added_on', 'last_contacted_at', 'latest_reply_sentiment_uuid', 'current_step_type', 'latest_task_done_at', 'created_at')},
        ),
    ]
