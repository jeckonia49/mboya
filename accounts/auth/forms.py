from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "id": "exampleInputEmail1"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"id": "exampleInputPassword1", "class": "form-control"}))


# class RegisterForm(forms.Form):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
#     password = forms.CharField(widget=forms.PasswordInput())
