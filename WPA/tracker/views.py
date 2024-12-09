from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Project, AttendanceEvent, Associate, Team

#utils 
from tracker.utils import fiscal_calendar_utils as du 

#forms 
from .forms import CreateTeamForm, ShiftTimeForm

# Create your views here.


def projects_overview(request):
	#wireframe 1
	if request.method == "GET":
		user = request.user
		authorized_projects = user.authorized_projects.all() 
		context = {"projects":authorized_projects}
		return render(request, 'attendance_tracker_overview.html', context)


def create_attendance_tracker(request):
	#wireframe 2
	if request.method == "GET":
		return render(request, 'create_attendance_tracker.html')


def attendance_tracker_view(request, project_pk): 
	#wireframe 3
	if request.method == "GET":
		project = Project.objects.get(pk=project_pk)
		teams = Team.objects.filter(project=project) 
		create_team_form = CreateTeamForm()
		shift_time_form = ShiftTimeForm()
		context = {"project":project, "teams":teams, "create_team_form":create_team_form, "shift_time_form":shift_time_form}
		import pdb; pdb.set_trace()
		return render(request, 'attendance_tracker_view.html', context)



def team_attendance_view(request, project_pk, team_pk): 
	#wireframe 4
	if request.method == "GET":
		return render(request, 'team_attendance_view.html')



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
		associate = Associate.objects.filter(pk=4).first()  # hard code associate pk for test. 
		events = AttendanceEvent.objects.filter(associate=associate).order_by("created_at") #oldest attendance events first

		
		weeks_to_populate = du.weeks_to_populate(events) 
		days_formatted, days_raw = du.days_to_populate(weeks_to_populate) #([datetime], [str])
	   # Create FiscalWeekDayData objects
		week_day_data_objects_list = []
		
		for day_raw, day_formatted in zip(days_raw, days_formatted):
			# Create the FiscalWeekDayData object and append to the list
			week_day_data = du.FiscalWeekDayData(day_raw=day_raw, day_formatted=day_formatted) 
			week_day_data_objects_list.append(week_day_data)

		for wdd_instance in week_day_data_objects_list:
			wdd_instance.associate_day_with_event(events)

		for wdd_instance in week_day_data_objects_list:
			wdd_instance.set_week()


		#Initialize FiscalWeek classes. Create a dict of FiscalWeeks. Loop through wdd_instances. If its week is not represented by  a FiscalWeek class, create one, add all wdd_instances with the week to its FiscalWeek class.
		fiscal_week_dict = du.create_fiscal_week_objects(week_day_data_objects_list) 


		

		# Add to context
		context = {'associate': associate, 'weeks_to_populate':weeks_to_populate, 'fiscal_week_dict':fiscal_week_dict}
		return render(request, 'associate_attendance_view.html', context)


def team_headcount_view(request, team_pk): 
	#wireframe 10
	if request.method == "GET":
		team = Team.objects.filter(pk=team_pk).first() #hardcode for test
		events = AttendanceEvent.objects.all().filter(team=team).order_by("created_at") # all attendance events for this team
		weeks_to_populate = du.weeks_to_populate(events) #all weeks those attendance events belong to
		weeks_to_populate = weeks_to_populate[::-1] #reverse slice ensures that the most recent week is populated first. 
		#days_formatted, days_raw = du.days_to_populate(weeks_to_populate)  #All the days in all of the weeks. days_raw is an array of datetime objects days_formatted is an array of string

		team_headcount_week_dict = {} 
		for week in weeks_to_populate: 

			team_headcount_week = du.TeamHeadCountWeek(week=week)
			team_headcount_week.team_week_day_data = du.TeamWeekDayData(week=week) 
			team_headcount_week_dict[week] = team_headcount_week

		
		
		for team_headcount_week in team_headcount_week_dict.values():
			twdd = team_headcount_week.team_week_day_data #This attribute holds the days and events of the weeks
			days_formatted = du.get_this_weeks_days_formatted(twdd.week)
			days_raw = du.get_this_weeks_days_raw(twdd.week)
			twdd.days_formatted = days_formatted 
			twdd.days_raw = days_raw 
			filtered_events = du.associate_TWDD_with_events(twdd, events)
			twdd.events = filtered_events
			twdd.set_days_workers_tally() 
			team_headcount_week.set_average_headcount()



		
		

		
		context = {"weeks_to_populate":weeks_to_populate, "team_headcount_week_dict":team_headcount_week_dict}
		return render(request, 'team_headcount_view.html', context)


def project_headcount_view(request, project_pk): 
	#wireframe 11
	if request.method == "GET":

		events = AttendanceEvent.objects.all().order_by("created_at") # all attendance events for this team
		weeks_to_populate = du.weeks_to_populate(events) #all weeks those attendance events belong to
		weeks_to_populate = weeks_to_populate[::-1] #reverse slice ensures that the most recent week is populated first. 
		#days_formatted, days_raw = du.days_to_populate(weeks_to_populate)  #All the days in all of the weeks. days_raw is an array of datetime objects days_formatted is an array of string

		team_headcount_week_dict = {} 
		for week in weeks_to_populate: 

			team_headcount_week = du.TeamHeadCountWeek(week=week)
			team_headcount_week.team_week_day_data = du.TeamWeekDayData(week=week) 
			team_headcount_week_dict[week] = team_headcount_week

		
		
		for team_headcount_week in team_headcount_week_dict.values():
			twdd = team_headcount_week.team_week_day_data #This attribute holds the days and events of the weeks
			days_formatted = du.get_this_weeks_days_formatted(twdd.week)
			days_raw = du.get_this_weeks_days_raw(twdd.week)
			twdd.days_formatted = days_formatted 
			twdd.days_raw = days_raw 
			filtered_events = du.associate_TWDD_with_events(twdd, events)
			twdd.events = filtered_events
			twdd.set_days_workers_tally() 
			team_headcount_week.set_average_headcount()

		context = {"weeks_to_populate":weeks_to_populate, "team_headcount_week_dict":team_headcount_week_dict}

		return render(request, 'project_headcount_view.html', context) 


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
		events = AttendanceEvent.objects.filter(associate=associate).order_by("created_at") #oldest attendance events first

		
		weeks_to_populate = du.weeks_to_populate(events) 
		weeks_to_populate = weeks_to_populate[::-1] #reverse slice ensures that the most recent week is populated first.
		days_formatted, days_raw = du.days_to_populate(weeks_to_populate) #([datetime], [str])
	   # Create FiscalWeekDayData objects
		week_day_data_objects_list = []
		
		for day_raw, day_formatted in zip(days_raw, days_formatted):
			# Create the FiscalWeekDayData object and append to the list
			week_day_data = du.FiscalWeekDayData(day_raw=day_raw, day_formatted=day_formatted) 
			week_day_data_objects_list.append(week_day_data)

		for wdd_instance in week_day_data_objects_list:
			wdd_instance.associate_day_with_event(events)

		for wdd_instance in week_day_data_objects_list:
			wdd_instance.set_week()


		#Initialize FiscalWeek classes. Create a dict of FiscalWeeks. Loop through wdd_instances. If its week is not represented by  a FiscalWeek class, create one, add all wdd_instances with the week to its FiscalWeek class.
		fiscal_week_dict = du.create_fiscal_week_objects(week_day_data_objects_list) 




		# Add to context
		context = {'associate': associate, 'weeks_to_populate':weeks_to_populate, 'fiscal_week_dict':fiscal_week_dict}
		
		return render(request, 'calendar.html', context)



		return render(request, 'project_headcount_view.html')


