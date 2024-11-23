from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import AttendanceEvent 

#utils 
from .utils.calendar_util import Calendar
# Create your views here.


def attendance_tracker_overview(request):
	#wireframe 1
	if request.method == "GET":
		return render(request, 'attendance_tracker_overview.html')


def create_attendance_tracker(request):
	#wireframe 2
	if request.method == "GET":
		return render(request, 'create_attendance_tracker.html')


def attendance_tracker_view(request): 
	#wireframe 3
	if request.method == "GET":
		return render(request, 'attendance_tracker_view.html')



def group_attendance_view(request): 
	#wireframe 4
	if request.method == "GET":
		return render(request, 'group_attendance_view.html')



def associate_detail_view(request): 
	#wireframe 5
	if request.method == "GET":
		return render(request, 'associate_detail_view.html')


def event_timeline_view(request): 
	#wireframe 6
	if request.method == "GET":
		return render(request, 'event_timeline.html')



def manage_associates_view(request): 
	#wireframe 7 
	if request.method == "GET":
		return render(request, 'manage_associates_view.html')



def user_alerts_view(request): 
	#wireframe 8
	if request.method == "GET":
		return render(request, 'user_alerts_view.html')


def associate_attendance_view(request): 
	#wireframe 9
	if request.method == "GET":
		return render(request, 'associate_attendance_view.html', context)


def group_headcount_view(request): 
	#wireframe 10
	if request.method == "GET":
		return render(request, 'group_headcount_view.html')


def project_headcount_view(request): 
	#wireframe 11
	if request.method == "GET":
		return render(request, 'project_headcount_view.html') 


#test views for developing calendar



class CalendarView(generic.ListView):
	model = AttendanceEvent
	template_name = 'calendar.html' 
	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs) 
		current_day = datetime.now().day
		current_month = datetime.now().month
		current_year = datetime.now().year
		
		# Initialize the Calendar class from the calendar module
		cal = Calendar()
		
		# Generate the HTML for the current month and year
		html_cal = cal.formatmonth(current_year, current_month, withyear=True)
		
		# Add the calendar to the context
		context['calendar'] = mark_safe(html_cal)
		
		# Optional: Add logic for 'next_month' if needed
		# context['next_month'] = next_month_logic_here
		
		return context

