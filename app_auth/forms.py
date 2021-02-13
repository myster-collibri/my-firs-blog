from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Nom utilisateur",widget=forms.TextInput(attrs={"class":"form-control"}))
    #declare le type du champ et on lui ajoute des attribut
    pwd=forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegesterForm(forms.Form):
    username=forms.CharField(label="Nom utilisateur",widget=forms.TextInput(attrs={"class":"form-control"}))
    #declare le type du champ et on lui ajoute des attribut
    pwd=forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    pwd_confirm=forms.CharField(label="Mot de passe confirmation",widget=forms.PasswordInput(attrs={'class':'form-control'}))

