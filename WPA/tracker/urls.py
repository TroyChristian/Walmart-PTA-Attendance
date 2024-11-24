from django.urls import path, include, reverse_lazy

#tracker
from . import views 

urlpatterns = [  

path('trackers', views.attendance_tracker_overview, name="trackers"),
path('create', views.create_attendance_tracker, name="create"),
path('tracker/<uuid:tracker_pk>', views.attendance_tracker_view, name="tracker"),
path('tracker/<uuid:tracker_pk>/group/<uuid:group_pk>', views.group_attendance_view, name="group_attendance"), #TODO take_attendance_view
path('associates/<int:associate_pk>', views.associate_detail_view, name="associate_detail"),
path('associates/<int:associate_pk>/timeline', views.event_timeline_view, name="timeline"),
path('tracker/manage_associates', views.manage_associates_view, name="manage_associates"),
path('alerts', views.user_alerts_view, name="alerts"),
path('tracker/<uuid:tracker_pk>/associate/<int:associate_pk>/attendance', views.associate_attendance_view, name="associate_attendance"),
path('tracker/<uuid:tracker_pk>/<uuid:group_pk>/headcount', views.group_headcount_view, name="group_headcount"),
path('tracker/<uuid:tracker_pk>/headcount', views.project_headcount_view, name="project_headcount"),

## Test routes for developing the calendar views ## 
path('calendar/vanilla', views.CalendarView.as_view(), name="vanilla_calendar"),








]