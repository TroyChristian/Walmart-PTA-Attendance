from django.contrib import admin
from . import models




class ProjectAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Project._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 

class CertificationAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Certification._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 

class AssociateAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Associate._meta.get_fields() if field.many_to_many != True and field.one_to_many != True]

class ShiftTimeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.ShiftTime._meta.get_fields() if field.many_to_many != True and field.one_to_many != True]

class TeamAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Team._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 


class CommentAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Comment._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 


class DisciplinaryActionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.DisciplinaryAction._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 

class AttendanceEventLegendAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.AttendanceEventLegend._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 



class AttendanceEventLegendAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.AttendanceEventLegend._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 

class AttendanceEventAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.AttendanceEvent._meta.get_fields() if field.many_to_many != True and field.one_to_many != True] 

class AlertAdmin(admin.ModelAdmin):
	list_display = [field.name for field in models.Alert._meta.get_fields() if field.many_to_many != True and field.one_to_many != True]


# Register your models here.
admin.site.register(models.Project, ProjectAdmin) 
admin.site.register(models.Certification, CertificationAdmin)
admin.site.register(models.Associate, AssociateAdmin) 
admin.site.register(models.ShiftTime, ShiftTimeAdmin) 
admin.site.register(models.Team, TeamAdmin) 
admin.site.register(models.Comment, CommentAdmin) 
admin.site.register(models.DisciplinaryAction, DisciplinaryActionAdmin) 
admin.site.register(models.AttendanceEventLegend, AttendanceEventLegendAdmin) 
admin.site.register(models.AttendanceEvent, AttendanceEventAdmin)

