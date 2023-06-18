import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vervetel.settings')

import django
django.setup()

from main.models import *
import datetime

year = 2023
months = [6,7,8,9,10,11,12]
days = range(1,30)

hours = range(6,13)
minutes = [00,30]

for i in months:
    for a in days:
        current_date = datetime.date(year=year, month=i, day=a)
        for t in hours:
            for m in minutes:
                current_time = datetime.time(hour=t, minute=m)

                DateTimes.objects.create(all_date=current_date, all_time=current_time)




