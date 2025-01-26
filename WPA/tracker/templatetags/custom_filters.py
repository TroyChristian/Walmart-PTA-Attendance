from django import template

register = template.Library()

@register.filter('get_item')
def get_item(dictionary, key):
	return dictionary.get(key) 

@register.filter('week_only')
def week_only(year_week_code):
	return year_week_code[4:]