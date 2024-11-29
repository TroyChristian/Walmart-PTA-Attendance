from django import forms

class CreateProjectForm(forms.ModelForm):
	#store # 
	#store address
	pass 


class GrantAccessForm(forms.ModelForm):
	#searchbar
	
	pass 


class CreateTeamForm(forms.ModelForm):
	#team name
	
	pass  

class EditTeamForm(forms.ModelForm):
	pass 


class CreateAssociateForm(forms.ModelForm):
	pass 

class EditAssociateNameForm(forms.ModelForm):
	pass

class CreateShiftForm(forms.ModelForm): 
	#shift start
	#shift end
	pass


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
