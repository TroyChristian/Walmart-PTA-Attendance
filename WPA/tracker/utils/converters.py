#custom convertors
from datetime import datetime
from django.urls import register_converter

class DateConverter:
	regex = r'\d{4}-\d{2}-\d{2}'

	def to_python(self, value):
		# Convert the string to a datetime object, then return only the date part
		return datetime.strptime(value, '%Y-%m-%d').date()

	def to_url(self, value):
		# Convert the date back to a string format for the URL
		return value.strftime('%Y-%m-%d')

register_converter(DateConverter, 'date')