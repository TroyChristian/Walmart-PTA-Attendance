from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import AttendanceEvent, Associate

#utils 
from tracker.utils import fiscal_calendar_utils as du 

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
	template_name = 'vanilla_calendar.html' 
	

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

def calendar(request):
	if request.method == "GET":
		associate = Associate.objects.filter(pk=4).first()  # hard code associate pk for test. 
		events = AttendanceEvent.objects.filter(associate=associate)
		first_event = associate.get_associate_earliest_event() #have to account for if there is no first event in real view.

		date_earliest_event = first_event.created_at.date()
		today_date = datetime.now().date()

		current_walmart_week = du.get_walmart_fiscal_year_and_week(today_date, week_only=True)
		first_event_walmart_week = du.get_walmart_fiscal_year_and_week(date_earliest_event, week_only=True)

		weeks_to_populate = [x for x in range(int(first_event_walmart_week), int(current_walmart_week) + 1)]
		
		context = {'associate':associate, 'events':events, 'date_earliest_event':date_earliest_event, 'today_date':today_date, 'current_walmart_week':current_walmart_week, 'first_event_walmart_week':first_event_walmart_week, 'weeks_to_populate':weeks_to_populate}

		
		return render(request, 'calendar.html', context) 

			


