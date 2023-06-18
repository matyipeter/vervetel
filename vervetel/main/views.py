from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm, DateTimes
from .models import Patients
import datetime

# Create your views here.

def indexpage(request):
	if request.method == 'POST':
		date = datetime.date(year=2023, month=int(request.POST['dateselect']), day=int(request.POST['dayselect']))
		time = request.POST['appselect']
		form = PatientForm(data=request.POST, date=date, time=time)
		if form.is_valid():
			user = form.save()		
		else:
			print(PatientForm.errors)

	else:
		user = PatientForm




	dates = set([i.all_date.month for i in DateTimes.objects.all()])
	
	days = set([i.all_date.day for i in DateTimes.objects.all()])
	
	appointments = set([i.all_time for i in DateTimes.objects.all()])
	appointments = sorted(appointments)
	
	
	return render(request, 'main/index.html', context={'form':user, 'dates':dates, 'days':days, 'app':appointments})


def datetimepicker(request):
	pass


