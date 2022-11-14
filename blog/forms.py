from django import forms 
from .models import Agent

class AgentForm(forms.ModelForm):
	class Meta:
		model = Agent
		fields = ['username', 'surname', 'age', 'nationality', 'cni', 'town']
		labels = {'username':'Nom', 'surname': 'Prénom', 'age':'Age','nationality':'Nationalité', 'cni':'N° CNI', 'town':'Résidence'}
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'surname':forms.TextInput(attrs={'class':'form-control'}),
			'age':forms.NumberInput(attrs={'class':'form-control'}),
			'nationality':forms.TextInput(attrs={'class':'form-control'}),
			'cni':forms.TextInput(attrs={'class':'form-control'}),
			'town':forms.TextInput(attrs={'class': 'form-control'}),
			
		}

class ClientForm(forms.ModelForm):
	class Meta:
		model = Agent
		fields = ['username', 'surname', 'age', 'nationality', 'town', 'cni']
		labels = {'username':'Nom', 'surname': 'Prénom', 'age':'Age','nationality':'Nationalité', 'town':'Ville', 'cni':'N° CNI'}
		widgets = {
			'username':forms.TextInput(attrs={'class':'form-control'}),
			'surname':forms.TextInput(attrs={'class':'form-control'}),
			'age':forms.NumberInput(attrs={'class':'form-control'}),
			'nationality':forms.TextInput(attrs={'class':'form-control'}),
			'town':forms.TextInput(attrs={'class': 'form-control'}),
			'cni':forms.TextInput(attrs={'class':'form-control'}),
			
			
		}