from django import forms

class registrationForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Enter your username"
        }),
        label="Username"
    )
    email = forms.EmailField(
        required=False,
        widget = forms.EmailInput(attrs={
            "class":"form-control",
            "placeholder":"example@gmail.com"
        }),
        label="Email"
    )
    password = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
        }),
        label="Password"
    )
    again_password = forms.CharField(
        min_length=8,
        required=True,
        widget=forms.PasswordInput(attrs={
            "class":"form-control",
        }),
        label="Re-enter Password"
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your username"
        }),
        label="Username"
    )
    password = forms.CharField(
        required=True,
        min_length=8,
        widget = forms.PasswordInput(attrs={
            "class":"form-control"
        }),
        label="Password"
    )

class ProfileForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Username"
        }),
        label="Username"
    )
    image = forms.ImageField(
        required=False,
        label="Profile Image"
    )
    loc = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Location"
        }),
        label="Location"
    )