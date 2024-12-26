from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from phonenumber_field.formfields import PhoneNumberField

from . import models


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.BaseUser
        fields = ('phonenumber',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.BaseUser
        fields = ('phonenumber',)


class CustomSuperUserCreationForm(UserCreationForm):
    class Meta:
        model = models.SuperUser
        fields = ('phonenumber',)


class CustomSuperUserChangeForm(UserChangeForm):
    class Meta:
        model = models.SuperUser
        fields = ('phonenumber',)


class CustomDoctorUserCreationForm(UserCreationForm):
    class Meta:
        model = models.DoctorUser
        fields = ('phonenumber',)


class CustomDoctorUserChangeForm(UserChangeForm):
    class Meta:
        model = models.DoctorUser
        fields = ('phonenumber',)


class CustomCommonUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CommonUser
        fields = ('phonenumber',)


class CustomCommonUserChangeForm(UserChangeForm):
    class Meta:
        model = models.CommonUser
        fields = ('phonenumber',)


class LoginForm(forms.Form):
    username = PhoneNumberField(region='IR')
    password = forms.CharField()
    remember_me = forms.BooleanField(required=False)
