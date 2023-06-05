import sys
from django.conf import settings
import requests
from datetime import datetime
from django.http import HttpResponse

from smartreachapi.models import Prospects

def fetch_campaigns_data():
    headers = {
        "X-API-KEY": settings.X_API_KEY
    }
    total=0
    page=1
    while True:
        response = requests.get(settings.API_URL_PROSPECTS+str(page), headers=headers)
        print('response')
        data = response.json()
            # print(data)
            # print(type(data))
            # print(len(data['data']['prospects']))
        data_used = data['data']['prospects']
        if len(data_used) > 0:
        # print(datetime.now())
            
            for i in range(len(data_used)):
                reqd_data = data_used[i]
                prospects_data = {
                    "prospect_id": reqd_data['id'],
                    "email": reqd_data['email'],
                    "first_name": reqd_data['first_name'],
                    "last_name": reqd_data['last_name'],
                    "category": reqd_data['prospect_category'],
                    "owner": reqd_data['owner_id'],
                    "team": reqd_data['team_id'],
                    "list": reqd_data['list'],
                    "company": reqd_data['company'],
                    "city": reqd_data['city'],
                    "state": reqd_data['state'],
                    "phone": reqd_data['phone'],
                    "job_title": reqd_data['job_title'],
                    "linkedin_url": reqd_data['linkedin_url'],
                    "country": reqd_data['country'],
                    "time_zone": reqd_data['timezone'],
                    "added_on": reqd_data['created_at'],
                    "last_contacted_at": reqd_data['last_contacted_at'],
                    "latest_reply_sentiment_uuid": reqd_data['latest_reply_sentiment_uuid'],
                    "current_step_type": reqd_data['current_step_type'],
                    "latest_task_done_at": reqd_data['latest_task_done_at']
                }
                prospect, created = Prospects.objects.update_or_create(**prospects_data)
                if created:
                    print('Created', prospect)
                    total+=1
            page+=1
        else:
            break
        
        
        # r.text, r.content, r.url, r.json
    print('done:', page, total)
    return HttpResponse(response.text)
    #return HttpResponse('Could not save data')
