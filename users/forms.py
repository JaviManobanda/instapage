from django import forms
from django.contrib.auth.models import User
from users.models import Profile


def attribute(placeholder):
    atributtes = {
        'placeholder': 'Last name',
        'class': 'form-control',
        'required': True
    }

    atributtes['placeholder'] = placeholder
    return atributtes


class SignupForm(forms.Form):

    username = forms.CharField(
        min_length=4, max_length=50, widget=forms.TextInput(attrs=attribute('username')))
    password = forms.CharField(
        max_length=70, widget=forms.PasswordInput(attrs=attribute('password')))
    password_confirmation = forms.CharField(
        max_length=70, widget=forms.PasswordInput(attrs=attribute('password confirm')))

    first_name = forms.CharField(
        min_length=2, max_length=50, widget=forms.TextInput(attrs=attribute('first name')))
    last_name = forms.CharField(
        min_length=2, max_length=50,  widget=forms.TextInput(attrs=attribute('last name')))
    email = forms.CharField(min_length=6, max_length=70,
                            widget=forms.EmailInput(attrs=attribute('last name')))

    def clean_username(self):
        """Unique username
        """
        # ? toma el dato q enviaste
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise forms.ValidationError('User is already in use.')
        return username  # ! siempre regresar el campo

    def clean(self):
        """Verified password confirmation match
        """
        data = super().clean()  # ! devuelve un diccionario
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password confirmation do not match')
        return data

    def save(self):
        data = super().clean()
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
