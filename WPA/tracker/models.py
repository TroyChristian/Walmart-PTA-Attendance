from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from datetime import datetime, time 

class Project(models.Model):
	store_number = models.PositiveIntegerField()
	address = models.CharField(max_length=255)
	STATUS_CHOICES = [
		('PENDING', 'Pending'),
		('ACTIVE', 'Active'),
		('ON_HOLD', 'On Hold'),
		('COMPLETED', 'Completed'),
		('CANCELLED', 'Cancelled')
	]
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
	associates = models.ManyToManyField('Associate', related_name='projects', blank=True, null=True)
	authorized_users = models.ManyToManyField(User, related_name='authorized_projects')
	created_by = models.ForeignKey(
		User,
		on_delete=models.PROTECT,
		related_name='user_projects'
	)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Project Store #{self.store_number} - {self.address}" 


	#Consider junction table for unique together (store_number, status=ACTIVE)
class Certification(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	
	def __str__(self):
		return self.name 

class ShiftTime(models.Model):
	start_time = models.TimeField()
	end_time = models.TimeField()
	
	def __str__(self):
		return f"{self.format_time(self.start_time)} - {self.format_time(self.end_time)}"
	
	@staticmethod
	def format_time(t):
		"""Convert time to 12-hour format with AM/PM"""
		return t.strftime("%I:%M%p").lstrip("0").lower()
	
	def is_earlier_than(self, other_shift):
		"""Compare if this shift starts earlier than another shift"""
		return self.start_time < other_shift.start_time


class Team(models.Model):
	team_name = models.CharField(max_length=100)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams',)
	shift_time = models.ManyToManyField(ShiftTime, related_name='shift_times')
	#associates = models.ForeignKey(Associate, on_delete=models.PROTECT, related_name='team')

	def __str__(self):
		return f"{self.team_name}"




class Associate(models.Model):
	name = models.CharField(max_length=100)
	points = models.DecimalField(
		max_digits=3,
		decimal_places=1,
		default=0
	) #save points as a value on the class so we are not calling calculate_attendance_points every time we need to display an associates points.
	deducted_points = models.DecimalField(
		max_digits=3,
		decimal_places=1,
		default=0
	)#track how many points have been decucted by management so we can subtract this amount from the result of calculate_attendance_points
	certifications = models.ManyToManyField(Certification, related_name='associates', null=True, blank=True) 
	team = models.ForeignKey(
		Team, 
		on_delete=models.PROTECT,  # Protect the team from deletion if it has associates
		null=True,
		blank=True,
		related_name='associates'  # Allows reverse access from Team to Associates
	)

	def __str__(self):
		return self.name


	def calculate_attendance_points(self):
		"""Calculate total attendance points for the associate"""
		return self.attendance_events.aggregate(
			total_points=models.Sum('point_value')
		)['total_points'] or 0






class BaseComment(models.Model):
	"""Abstract base class for Comment and DisciplinaryAction"""
	COMMENT_TYPES = [
		('POSITIVE', 'Positive'),
		('INFORMATIONAL', 'Informational'),
		('COACHING', 'Coaching')
	]
	
	content = models.TextField()
	comment_type = models.CharField(max_length=20, choices=COMMENT_TYPES)
	associate = models.ForeignKey(Associate, on_delete=models.CASCADE)
	witnessed_by = models.ManyToManyField(
		User,
		related_name='%(class)s_witnessed', 
		null = True, 
		blank = True
	)
	alerted_users = models.ManyToManyField(
		User,
		related_name='%(class)s_alerts',
		null = True, 
		blank = True
	)
	created_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(
		User,
		on_delete=models.PROTECT,
		related_name='%(class)s_created',
		null = True, 
		blank = True
	)
	
	class Meta:
		abstract = True

class Comment(BaseComment):
	def __str__(self):
		return f"Comment for {self.associate.name} - {self.created_at}"

class DisciplinaryAction(BaseComment):
	def __str__(self):
		return f"Disciplinary Action for {self.associate.name} - {self.created_at}"

class AttendanceEventLegend(models.Model):
	code = models.CharField(max_length=4, unique=True)
	description = models.CharField(max_length=50)
	point_value = models.DecimalField(
		max_digits=3,
		decimal_places=1,
		default=0
	)
	
	class Meta:
		ordering = ['code']
	
	def __str__(self):
		return f"{self.code}: {self.description} ({self.point_value} points)"

	@classmethod
	def create_defaults(cls):
		"""Create default attendance event types"""
		defaults = [
			('W', 'Worked', 0),
			('PTO', 'PTO', 0),
			('PPTO', 'PPTO', 0),
			('LOA', 'LOA', 0),
			('OFF', 'Off', 0),
			('EI', 'Early In', 0.5),
			('EO', 'Early Out', 0.5),
			('IS', 'Incomplete Shift', 1),
			('A', 'Absent', 1),
			('NC', 'No Call/No Show', 3),
			('KD', 'Key Date Event', 2),
		]
		for code, desc, points in defaults:
			cls.objects.get_or_create(
				code=code,
				defaults={'description': desc, 'point_value': points}
			) 

#TODO# Unique Together AttendanceEventLegend, Project

class AttendanceEvent(models.Model):
	event = models.ForeignKey(
		AttendanceEventLegend,
		on_delete=models.PROTECT,
		related_name='attendance_events'
	)
	associate = models.ForeignKey(
		Associate,
		on_delete=models.CASCADE,
		related_name='attendance_events'
	)
	created_by = models.ForeignKey(
		User,
		on_delete=models.PROTECT,
		related_name='created_attendance_events'
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	updated_by = models.ForeignKey(
		User,
		on_delete=models.PROTECT,
		related_name='updated_attendance_events',
		null=True,
		blank=True
	)

	@property
	def point_value(self):
		"""Get point value from the associated legend entry"""
		return self.event.point_value

	def __str__(self):
		return f"{self.associate.name} - {self.event.code} on {self.created_at.date()}"

class Alert(models.Model):
	content_type = models.ForeignKey('contenttypes.ContentType', on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	alerter = GenericForeignKey('content_type', 'object_id')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
	created_at = models.DateTimeField(auto_now_add=True)
	is_seen = models.BooleanField(default=False)

	def __str__(self):
		return f"Alert for {self.user.username} - {self.created_at}"
	










