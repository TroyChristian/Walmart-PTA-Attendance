"""Functions and classes for testing and development """ 

import time
import datetime
from collections import namedtuple
# Constants




walmart_fiscal_weeks = {
	2024: {
		43: ['11-16-2024', '11-17-2024', '11-18-2024', '11-19-2024', '11-20-2024', '11-21-2024', '11-22-2024'],
		44: ['11-23-2024', '11-24-2024', '11-25-2024', '11-26-2024', '11-27-2024', '11-28-2024', '11-29-2024'],
		45: ['11-30-2024', '12-01-2024', '12-02-2024', '12-03-2024', '12-04-2024', '12-05-2024', '12-06-2024'],
		46: ['12-07-2024', '12-08-2024', '12-09-2024', '12-10-2024', '12-11-2024', '12-12-2024', '12-13-2024'],
		47: ['12-14-2024', '12-15-2024', '12-16-2024', '12-17-2024', '12-18-2024', '12-19-2024', '12-20-2024'],
		48: ['12-21-2024', '12-22-2024', '12-23-2024', '12-24-2024', '12-25-2024', '12-25-2024', '12-26-2024', '12-27-2024'],
		49: ['12-28-2024', '12-29-2024', '12-30-2024', '12-31-2024', '01-01-2025', '01-02-2025', '01-03-2025'],
		50: ['01-04-2025', '01-05-2025', '01-06-2025', '01-07-2025', '01-08-2025', '01-09-2025', '01-10-2025'],
		51: ['01-11-2025', '01-12-2025', '01-13-2025', '01-14-2025', '01-15-2025', '01-16-2025', '01-17-2025'],
		52: ['01-18-2025', '01-19-2025', '01-20-2025', '01-21-2025', '01-22-2025', '01-23-2025', '01-24-2025'],
		53: ['01-25-2025', '01-26-2025', '01-27-2025', '01-28-2025', '01-29-2025', '01-30-2025', '01-31-2025']
	},
	2025: {
		1: ['02-01-2025', '02-02-2025', '02-03-2025', '02-04-2025', '02-05-2025', '02-06-2025', '02-07-2025'],
		2: ['02-08-2025', '02-09-2025', '02-10-2025', '02-11-2025', '02-12-2025', '02-13-2025', '02-14-2025'],
		3: ['02-15-2025', '02-16-2025', '02-17-2025', '02-18-2025', '02-19-2025', '02-20-2025', '02-21-2025'],
		4: ['02-22-2025', '02-23-2025', '02-24-2025', '02-25-2025', '02-26-2025', '02-27-2025', '02-28-2025'],
		5: ['03-1-2025', '03-2-2025', '03-03-2025', '03-04-2025', '03-05-2025', '03-06-2025', '03-07-2025'],
		6: ['03-08-2025', '03-09-2025', '03-10-2025', '03-11-2025', '03-12-2025', '03-13-2025', '03-14-2025'],
		7: ['03-15-2025', '03-16-2025', '03-17-2025', '03-18-2025', '03-19-2025', '03-20-2025', '03-21-2025'],
		8: ['03-22-2025', '03-23-2025', '03-24-2025', '03-25-2025', '03-26-2025', '03-27-2025', '03-28-2025'],
		9: ['03-29-2025', '03-30-2025', '03-31-2025', '04-01-2025', '04-02-2025', '04-03-2025', '04-04-2025'],
		10: ['04-05-2025', '04-06-2025', '04-07-2025', '04-08-2025', '04-09-2025', '04-10-2025', '04-11-2025'],
		11: ['04-12-2025', '04-13-2025', '04-14-2025', '04-15-2025', '04-16-2025', '04-17-2025', '04-18-2025'],
		12: ['04-19-2025', '04-20-2025', '04-21-2025', '04-22-2025', '04-23-2025', '04-24-2025', '04-25-2025'],
		13: ['04-26-2025', '04-27-2025', '04-28-2025', '04-29-2025', '04-30-2025', '05-01-2025', '05-02-2025'],
		14: ['05-03-2025', '05-04-2025', '05-05-2025', '05-06-2025', '05-07-2025', '05-08-2025', '05-09-2025'],
		15: ['05-10-2025', '05-11-2025', '05-12-2025', '05-13-2025', '05-14-2025', '05-15-2025', '05-16-2025'],
		16: ['05-17-2025', '05-18-2025', '05-19-2025', '05-20-2025', '05-21-2025', '05-22-2025', '05-23-2025'],
		17: ['05-24-2025', '05-25-2025', '05-26-2025', '05-27-2025', '05-28-2025', '05-29-2025', '05-30-2025'],
		18: ['05-31-2025', '06-01-2025', '06-02-2025', '06-03-2025', '06-04-2025', '6-05-2025', '6-06-2025'],
		19: ['06-07-2025', '06-08-2025', '06-09-2025', '06-10-2025', '06-11-2025', '06-12-2025', '06-13-2025'],
		20: ['06-14-2025', '06-15-2025', '06-16-2025', '06-17-2025', '06-18-2025', '06-19-2025', '06-20-2025'],
		21: ['06-21-2025', '06-22-2025', '06-23-2025', '06-24-2025', '06-25-2025', '06-26-2025', '06-27-2025'],
		22: ['06-28-2025', '06-29-2025', '06-30-2025', '07-01-2025', '07-02-2025', '07-03-2025', '07-04-2025'],
		23: ['07-05-2025', '07-06-2025', '07-07-2025', '07-08-2025', '07-09-2025', '07-10-2025', '07-11-2025'],
		24: ['07-12-2025', '07-13-2025', '07-14-2025', '07-15-2025', '07-16-2025', '07-17-2025', '07-18-2025'],
		25: ['07-19-2025', '07-20-2025', '07-21-2025', '07-22-2025', '07-23-2025', '07-24-2025', '07-25-2025'],
		26: ['07-26-2025', '07-27-2025', '07-28-2025', '07-29-2025', '07-30-2025', '07-31-2025', '08-01-2025'],
		27: ['08-02-2025', '08-03-2025', '08-04-2025', '08-05-2025', '08-06-2025', '08-07-2025', '08-08-2025'],
		28: ['08-09-2025', '08-10-2025', '08-11-2025', '08-12-2025', '08-13-2025', '08-14-2025', '08-15-2025'],
		29: ['08-16-2025', '08-17-2025', '08-18-2025', '08-19-2025', '08-20-2025', '08-21-2025', '08-22-2025'],
		30: ['08-23-2025', '08-24-2025', '08-25-2025', '08-26-2025', '08-27-2025', '08-28-2025', '08-29-2025'],
		31: ['08-30-2025', '08-31-2025', '09-01-2025', '09-02-2025', '09-03-2025', '09-04-2025', '09-05-2025'],
		32: ['09-06-2025', '09-07-2025', '09-08-2025', '09-09-2025', '09-10-2025', '09-11-2025', '09-12-2025'],
		33: ['09-13-2025', '09-14-2025', '09-15-2025', '09-16-2025', '09-17-2025', '09-18-2025', '09-19-2025'],
		34: ['09-20-2025', '09-21-2025', '09-22-2025', '09-23-2025', '09-24-2025', '09-25-2025', '09-26-2025'],
		35: ['09-27-2025', '09-28-2025', '09-29-2025', '09-30-2025', '10-01-2025', '10-02-2025', '10-03-2025'],
		36: ['10-04-2025', '10-05-2025', '10-06-2025', '10-07-2025', '10-08-2025', '10-09-2025', '10-10-2025'],
		37: ['10-11-2025', '10-12-2025', '10-13-2025', '10-14-2025', '10-15-2025', '10-16-2025', '10-17-2025'],
		38: ['10-18-2025', '10-19-2025', '10-20-2025', '10-21-2025', '10-22-2025', '10-23-2025', '10-24-2025'],
		39: ['10-25-2025', '10-26-2025', '10-27-2025', '10-28-2025', '10-29-2025', '10-30-2025', '10-31-2025'],
		40: ['11-01-2025', '11-02-2025', '11-03-2025', '11-04-2025', '11-05-2025', '11-06-2025', '11-07-2025'],
		41: ['11-08-2025', '11-09-2025', '11-10-2025', '11-11-2025', '11-12-2025', '11-13-2025', '11-14-2025'],
		42: ['11-15-2025', '11-16-2025', '11-17-2025', '11-18-2025', '11-19-2025', '11-20-2025', '11-21-2025'],
		43: ['11-22-2025', '11-23-2025', '11-24-2025', '11-25-2025', '11-26-2025', '11-27-2025', '11-28-2025'],
		44: ['11-29-2025', '11-30-2025', '12-01-2025', '12-02-2025', '12-03-2025', '12-04-2025', '12-05-2025'],
		45: ['12-06-2025', '12-07-2025', '12-08-2025', '12-09-2025', '12-10-2025', '12-11-2025', '12-12-2025'],
		46: ['12-13-2025', '12-14-2025', '12-15-2025', '12-16-2025', '12-17-2025', '12-18-2025', '12-19-2025'],
		47: ['12-20-2025', '12-21-2025', '12-22-2025', '12-23-2025', '12-24-2025', '12-25-2025', '12-26-2025'],
		48: ['12-27-2025', '12-28-2025', '12-29-2025', '12-30-2025', '12-31-2025', '01-01-2025', '01-02-2025'],
		49: ['12-03-2025', '12-04-2025', '12-05-2025', '12-06-2025', '12-07-2025', '12-08-2025', '12-09-2025'],
		50: ['12-10-2025', '12-11-2025', '12-12-2025', '12-13-2025', '12-14-2025', '12-15-2025', '12-16-2025'],
		51: ['12-17-2025', '12-18-2025', '12-19-2025', '12-20-2025', '12-21-2025', '12-22-2025', '12-23-2025'],
		52: ['12-24-2025', '12-25-2025', '12-26-2025', '12-27-2025', '12-28-2025', '12-29-2025', '12-30-2025']
	}
} 

WeekDayData = namedtuple('WeekDayData', ['week', 'day_raw', 'day_formatted', 'event']) 

def get_walmart_fiscal_year_and_week(date, week_only=False) -> str:
	"""
	Given a date, return the Walmart fiscal year and fiscal week number in the format YYYYWW.
	""" 
	formatted_date = format_date(date) # so that date matches the dictionary format
	fiscal_year = date.year
	fiscal_week = None 


	# Search for the fiscal week in the dictionary
	for year, weeks in walmart_fiscal_weeks.items():
		for week, dates in weeks.items():
			if formatted_date in dates:
				fiscal_week = week
				break

	if fiscal_week is None:
		return "Week not found in fiscal year."  # Handle out-of-range dates

	# Return the formatted fiscal year and week
	if week_only:
		return str(fiscal_week)
	else:
		return f"{fiscal_year}{fiscal_week:02d}"


class FiscalWeekDayData:
	def __init__(self, week=None, day_raw=None, day_formatted=None, event=None):
		self.week = week #fiscal week
		self.day_raw =day_raw #datetime to map to event
		self.day_formatted = day_formatted #formatted day for display 
		self.event = event #stores AttendanceEvent
	
	def __str__(self): 
		return f"FiscalWeekDayData: week:{self.week} day:{self.day_formatted} event: {self.event}"

	def __repr__(self): 
		return f"FiscalWeekDayData: week:{self.week} day:{self.day_formatted} event: {self.event}"

	def associate_day_with_event(self, events):
		"""Check if an AttendanceEvent exists for a specific day."""
		for event in events:
			if event.created_at.date() == self.day_raw:  # Compare only the date part
				self.event = event
				break 
		return None  # No event found for this day 

	def set_week(self):
		self.week = get_walmart_fiscal_year_and_week(self.day_raw) 

	def __eq__(self, other):
		"""Custom equality check for FiscalWeekDayData."""
		if isinstance(other, FiscalWeekDayData):
			return (self.week == other.week and
					self.day_raw == other.day_raw and
					self.day_formatted == other.day_formatted)  # Compare relevant fields
		return False

	def __hash__(self):
		"""Override hash to match equality check."""
		return hash((self.week, self.day_raw, self.day_formatted))  # Based on fields that define equality

	def associate_day_with_event(self, events):
		"""Check if an AttendanceEvent exists for a specific day."""
		for event in events:
			if event.created_at.date() == self.day_raw:  # Compare only the date part
				self.event = event
				break
		return None  # No event found for this day




class FiscalWeek:
	def __init__(self, week=None, day_data_array=None): 
		self.week = week 
		self.day_data_array = day_data_array
	def __str__(self): 
		return f"FiscalWeek: week {self.week} day_data_array: {len(self.day_data_array)} FWDD objects in array"

	def __repr__(self): 
		return f"FiscalWeek: week {self.week} day_data_array: {len(self.day_data_array)} FWDD objects in array"
	



def create_fiscal_week_objects(fiscal_week_day_data_array): #Take in an array of FiscalWeekDayData whose event attribute is already set. This function groups FWDD objects into the days attribute of the FiscalWeek class so that evreything can be iterated over neatly in the template. 
	fiscal_week_dict = {} #The FWDD's week attr {wdd.week:FiscalWeek} There are 14 elements in fiscal_week_day_data_array
	#Create 6 digit week codes has dictionary key. 
	for wdd in fiscal_week_day_data_array:
		if wdd.week not in fiscal_week_dict:
			fiscal_week_dict[wdd.week] = FiscalWeek(week=wdd.week)
		else: 
			continue 
	for k in fiscal_week_dict.keys():
		days_array = []
		for wdd in fiscal_week_day_data_array:
			if wdd.week == k:
				days_array.append(wdd)
		print(days_array)
		fiscal_week_dict[k].day_data_array = days_array 
		print(fiscal_week_dict[k]) 
	return fiscal_week_dict

	








def zip_weeks_days_data(weeks_to_populate, days_raw, days_formatted, event_placeholders):
	
	merged_list = [WeekDayData(week, day_raw, day_formatted, event_placeholders)
				   for week, day_raw, day_formatted, placeholder in zip(weeks_to_populate, days_raw, days_formatted, event_placeholders)]
	return merged_list 

def create_fiscal_week_day_data_objects(weeks_to_populate, days_raw, days_formatted):
	week_day_data_objects_list = [FiscalWeekDayData(week, day_raw, day_formatted)
				   for week, day_raw, day_formatted in zip(weeks_to_populate, days_raw, days_formatted)]
	return week_day_data_objects_list

def format_date(event_created_at) -> str:
	#event_date = str(event_created_at.date()) #'2024-11-25', '02-02-2025'
	formatted_date = event_created_at.strftime('%m-%d-%Y')
	return formatted_date



def format_datetime_array(datetime_array) -> [str]:
	formatted_dates = [] 
	for date in datetime_array:
		formatted_dates.append(format_date(date))
	return formatted_dates 





# function 2: get_days_in_walmart_fiscal_week
def get_days_in_walmart_fiscal_week(fiscal_week_str: str):
	"""
	Given a Walmart fiscal week as a string in the format 'YYYYWW' (e.g., '202443'),
	return a list of dates in that week.
	"""
	# Extract the fiscal year and fiscal week from the input string
	fiscal_year = int(fiscal_week_str[:4])  # First 4 characters as the year
	fiscal_week = int(fiscal_week_str[4:])  # Last 2 characters as the week number
	
	# Search for the fiscal week in the dictionary
	if fiscal_year in walmart_fiscal_weeks and fiscal_week in walmart_fiscal_weeks[fiscal_year]:
		return [datetime.datetime.strptime(date_str, "%m-%d-%Y").date() for date_str in walmart_fiscal_weeks[fiscal_year][fiscal_week]]




def weeks_to_populate(events) -> [int]:
	weeks = []
	for event in events:
		week = get_walmart_fiscal_year_and_week(event.created_at)
		if len(week) == 6: #If a 6 character year/week combo is found in the dictionary
			weeks.append(week) 
	return weeks #this count is how many 7 day div rows we are going to populate the template with.


def days_to_populate(fiscal_week_numbers) -> [str]: #[str])
	days_array = [] 
	days_array_formatted = []
	for week in fiscal_week_numbers:
		days = get_days_in_walmart_fiscal_week(week)
		for day in days:
			days_array.append(day) #datetime object to remap events with the day
			days_array_formatted.append(format_date(day)) #formatted days to display
	return (days_array_formatted, days_array)

	






def get_attendance_event_year_week_walmart_fiscal_calendar(event, week_only=False):
	date = event.created_at.date() #convert datetime  object (created_at) to date for compatability with helper function. 
	return get_walmart_fiscal_year_and_week(date, week_only) 




# New Approach









