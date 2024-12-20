from django.urls import path, include, reverse_lazy
from .utils.converters import DateConverter
#tracker
from . import views 

urlpatterns = [  

path('', views.projects_overview, name="projects"),
path('create', views.create_attendance_tracker, name="create"),

path('tracker/<int:project_pk>', views.attendance_tracker_view, name="tracker"),
path('tracker/<int:project_pk>/<date:date>/', views.attendance_tracker_view, name="tracker"), #http://localhost:8000/tracker/1/2024-12-19
path('tracker/<int:project_pk>/team/<int:team_pk>', views.team_attendance_view, name="team_attendance"), #TODO take_attendance_view
path('associates/<int:associate_pk>', views.associate_detail_view, name="associate_detail"),
path('associates/<int:associate_pk>/timeline', views.event_timeline_view, name="timeline"),
path('tracker/manage_associates', views.manage_associates_view, name="manage_associates"),
path('alerts', views.user_alerts_view, name="alerts"),
path('tracker/<int:tracker_pk>/associate/<int:associate_pk>/attendance', views.associate_attendance_view, name="associate_attendance"),
path('tracker/team/headcount/<int:team_pk>', views.team_headcount_view, name="team_headcount"),
path('project/headcount/<int:project_pk>/', views.project_headcount_view, name="project_headcount"),


## Test routes for developing the calendar views ## 
path('calendar/vanilla', views.CalendarView.as_view(), name="vanilla_calendar"),
path('calendar', views.calendar, name="calendar")









] 

