from django import forms 
from .models import Team, ShiftTime

class CreateProjectForm(forms.ModelForm):
	#store # 
	#store address
	pass 


class GrantAccessForm(forms.ModelForm):
	#searchbar
	
	pass 


class CreateTeamForm(forms.ModelForm):
	team_name = forms.CharField(widget=forms.TextInput(attrs={'class':"align-text-center"})) 


	class Meta:
		model = Team
		exclude = ['project']
		fields = ['team_name', 'shift_time']
		widgets = {
			'description': forms.Textarea(attrs={'class': 'description'}),
		} 
	def __init__(self, *args, **kwargs):
		super(CreateTeamForm, self).__init__(*args, **kwargs)
		self.fields['shift_time'].label = "Select Shift Times for Team"  # Custom label for shift_time field




class EditTeamForm(forms.ModelForm):
	pass 


class CreateAssociateForm(forms.ModelForm):
	pass 

class EditAssociateNameForm(forms.ModelForm):
	pass


class ShiftTimeForm(forms.ModelForm):
	class Meta:
		model = ShiftTime
		fields = ['start_time', 'end_time']  # Include the fields that users will input
	
	# Optional: Add any custom validation or styling if needed
	start_time = forms.ChoiceField(
		choices=ShiftTime.TIME_CHOICES,
		required=True,
		widget=forms.Select(attrs={'class': 'form-select'}),
	)
	end_time = forms.ChoiceField(
		choices=ShiftTime.TIME_CHOICES,
		required=True,
		widget=forms.Select(attrs={'class': 'form-select'}),
	)


class AttendanceEventEditForm(forms.ModelForm):
	#options 
	pass 

class CommentForm(forms.ModelForm):
	#content 
	#witnessed by
	#created_by 
	#send_alert_to 
	#associate
	pass 

class DisciplinaryActionForm(forms.ModelForm):
	#content 
	#witnessed_by
	#send_alert_to 
	#created_by
	#associate 
	pass

class ReducePointForm(forms.ModelForm):
	#points 
	#associate 
	#created_by
	pass
