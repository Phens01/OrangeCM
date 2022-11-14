from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="Nom de l'Agent",widget=forms.TextInput(attrs={'class':'form-control'}))
	pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nom",widget=forms.TextInput(attrs={'class':'form-control'}))
	surname = forms.CharField(label="Prénom",widget=forms.TextInput(attrs={'class':'form-control'}))
	age = forms.CharField(label="Âge",widget=forms.NumberInput(attrs={'class':'form-control'}))
	town = forms.CharField(label="Ville",widget=forms.TextInput(attrs={'class':'form-control'}))
	cni = forms.CharField(label="CNI",widget=forms.TextInput(attrs={'class':'form-control'}))
	pwd = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	pwd_confirm = forms.CharField(label="Mot de passe de confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm0(forms.Form):
	username = forms.CharField(label="Nom",widget=forms.TextInput(attrs={'class':'form-control'}))
	surname = forms.CharField(label="Prénom",widget=forms.TextInput(attrs={'class':'form-control'}))
	town = forms.CharField(label="Ville",widget=forms.TextInput(attrs={'class':'form-control'}))
	cni = forms.CharField(label="CNI",widget=forms.TextInput(attrs={'class':'form-control'}))