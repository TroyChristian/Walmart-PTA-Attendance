from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import AttendanceEvent 

#utils 

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
		events = AttendanceEvent.objects.filter(associate=4)  # hard code associate pk for test.

		# Prepare events data in a format suitable for VanillaCalendarPro
		events_data = [
			{
				'date': event.created_at.strftime('%Y-%m-%d'),  # Format the date as string
				'color': '#00FF00'  # Pass the color for the event. Hardcode green for test.
			}
			for event in events
		]

		print(events_data)  # Add this line to print the events data for debugging

		# Pass the events data to the template context
		context['events'] = events_data

		return context
			


