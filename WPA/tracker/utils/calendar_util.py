from datetime import datetime, timedelta
from calendar import HTMLCalendar
from tracker.models import AttendanceEvent 
	
class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

