from django import forms 
from .models import Team, ShiftTime, Associate, Certification

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
			'team_name': forms.TextInput(attrs={'class': 'form-control'}),
			'shift_time': forms.SelectMultiple(attrs={'class': 'form-control'}),  # This allows multiple selections for shift_time
		}
	
	def __init__(self, *args, **kwargs):
		super(CreateTeamForm, self).__init__(*args, **kwargs)
		self.fields['shift_time'].label = "Select Shift Times for Team"  # Custom label for shift_time field


class EditTeamForm(forms.ModelForm):
	pass 


class CreateAssociateForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
	certifications = forms.ModelChoiceField(queryset=Certification.objects.all(), required=False, 
								   widget=forms.Select(attrs={'class': 'form-select'}))
	class Meta:
		model = Associate
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'certifications': forms.SelectMultiple(attrs={'class': 'form-control'}),  # This allows multiple selections for certifications
		}
	# def __init__(self, *args, **kwargs):
	# 	project = kwargs.pop('certifications', None)  # Retrieve the project context
	# 	super().__init__(*args, **kwargs)

class AssignTeamForm(forms.Form):
	teams = forms.ModelChoiceField(queryset=Team.objects.all(), required=True, 
								   widget=forms.Select(attrs={'class': 'form-select'}))
	def __init__(self, *args, **kwargs):
		project = kwargs.pop('project', None)  # Retrieve the project context
		super().__init__(*args, **kwargs)
		
		if project:
			self.fields['teams'].queryset = Team.objects.filter(project=project)

class AssignShiftTimeForm(forms.Form):
	shift_time = forms.ModelChoiceField(queryset=ShiftTime.objects.none(), required=True,
										widget=forms.Select(attrs={'class': 'form-select'}))

	def __init__(self, *args, **kwargs):
		shift_times = kwargs.pop('shift_times', None)  # Retrieve the shift_times context
		super().__init__(*args, **kwargs)

		if shift_times:
			self.fields['shift_time'].queryset = shift_times
			# Debugging: print the queryset for shift_time field


	def clean_shift_time(self):
		shift_time = self.cleaned_data.get('shift_time')  # This will now be the ShiftTime object
		if not shift_time:
			raise forms.ValidationError("Invalid shift time selected.")
		return shift_time

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
