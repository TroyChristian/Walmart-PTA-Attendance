"""Functions and classes for testing and development """ 

import tracker.models 

import datetime

# Constants
WEEKS_IN_FISCAL_YEAR = 52
WEEKS_IN_FISCAL_YEAR_LEAP = 53
DAYS_IN_FISCAL_YEAR = 364
DAYS_IN_FISCAL_YEAR_LEAP = 371

# Calculate Walmart Fiscal Year and Week
def get_walmart_fiscal_year_and_week(date, week_only=False): # passing an a datetime here going to
	"""
	Given a date, return the Walmart fiscal year and fiscal week number in the format YYYYWW.
	
	Walmart fiscal year starts on the first Saturday of the calendar week containing February 1st.
	Walmart fiscal weeks follow a 52-week structure, with an additional week added every 7 years for leap years.
	
	:param date: The date to be mapped to Walmart's fiscal year
	:return: A string representing the fiscal year and week in YYYYWW format
	"""
	
	# Step 1: Find the first Saturday of the week containing February 1st
	year = date.year
	feb_1 = datetime.date(year, 2, 1)
	
	# Calculate the first Saturday of the week that contains February 1st
	days_to_saturday = (5 - feb_1.weekday()) % 7  # 5 is Saturday
	fiscal_year_start = feb_1 + datetime.timedelta(days=days_to_saturday)
	
	# Step 2: Determine if the year is a 52-week or 53-week fiscal year
	if (fiscal_year_start - datetime.date(year, 1, 1)).days > DAYS_IN_FISCAL_YEAR:
		fiscal_year_length = DAYS_IN_FISCAL_YEAR_LEAP
		weeks_in_fiscal_year = WEEKS_IN_FISCAL_YEAR_LEAP
	else:
		fiscal_year_length = DAYS_IN_FISCAL_YEAR
		weeks_in_fiscal_year = WEEKS_IN_FISCAL_YEAR
	
	# Step 3: Calculate the fiscal week number
	delta_days = (date - fiscal_year_start).days
	fiscal_week = (delta_days // 7) + 1
	
	# Ensure fiscal week stays within the correct range (1-52 or 1-53)
	if fiscal_week > weeks_in_fiscal_year:
		fiscal_week = weeks_in_fiscal_year
	
	# Step 4: Return fiscal year and fiscal week in YYYYWW format
	fiscal_year = fiscal_year_start.year if date >= fiscal_year_start else fiscal_year_start.year - 1
	fiscal_year_week = f"{fiscal_year}{fiscal_week:02d}"
	
	if week_only:
		fiscal_week_formatted = f"{fiscal_week:02d}"
		return fiscal_week_formatted

	return fiscal_year_week



# Example usage:
date = datetime.date(2024, 11, 23)
fiscal_year_week = get_walmart_fiscal_year_and_week(date)

print(f"Date: {date}")
print(f"Walmart Fiscal Year and Week: {fiscal_year_week}") 

def get_attendance_event_year_week_walmart_fiscal_calendar(event, week_only=False):
	date = event.created_at.date() #convert datetime  object (created_at) to date for compatability with helper function. 
	return get_walmart_fiscal_year_and_week(date, week_only) 

def get_associates_earliest_event(associate):
	attendance_events = AttendanceEvent.objects.filter(pk=associate) 
	return attendance_events.order_by('created_at').first() 








