from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms, models


class CustomBaseUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm

    model = models.BaseUser

    list_display = ('phonenumber', 'is_active', 'last_login',)
    list_filter = ('is_active', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('phonenumber', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_phonenumber_confirmed',)}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phonenumber', 'password1', 'password2', 'is_active',
                       'is_phonenumber_confirmed', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('phonenumber',)
    ordering = ('phonenumber',)
    filter_horizontal = ()


class CustomSuperUserAdmin(UserAdmin):
    add_form = forms.CustomSuperUserCreationForm
    form = forms.CustomSuperUserChangeForm

    model = models.SuperUser

    list_display = ('phonenumber', 'is_active', 'last_login',)
    list_filter = ('is_active', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('phonenumber', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_phonenumber_confirmed',)}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phonenumber', 'password1', 'password2', 'is_active',
                       'is_phonenumber_confirmed', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('phonenumber',)
    ordering = ('phonenumber',)
    filter_horizontal = ()


class CustomDoctorUserAdmin(UserAdmin):
    add_form = forms.CustomDoctorUserCreationForm
    form = forms.CustomDoctorUserChangeForm

    model = models.DoctorUser

    list_display = ('phonenumber', 'is_active', 'last_login', 'city', 'expertise')
    list_filter = ('is_active', 'first_name', 'last_name', 'city', 'expertise')
    fieldsets = (
        (None, {'fields': ('phonenumber', 'password', 'first_name', 'last_name', 'city', 'expertise')}),
        ('Permissions', {'fields': ('is_active', 'is_phonenumber_confirmed',)}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phonenumber', 'password1', 'password2', 'is_active', 'city', 'expertise',
                       'is_phonenumber_confirmed', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('phonenumber', 'expertise')
    ordering = ('phonenumber',)
    filter_horizontal = ()


class CustomCommonUserAdmin(UserAdmin):
    add_form = forms.CustomCommonUserCreationForm
    form = forms.CustomCommonUserChangeForm

    model = models.CommonUser

    list_display = ('phonenumber', 'is_active', 'last_login', 'city', 'national_id')
    list_filter = ('is_active', 'first_name', 'last_name', 'city', 'national_id')
    fieldsets = (
        (None, {'fields': ('phonenumber', 'password', 'first_name', 'last_name', 'city', 'national_id')}),
        ('Permissions', {'fields': ('is_active', 'is_phonenumber_confirmed',)}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phonenumber', 'password1', 'password2', 'is_active', 'city', 'national_id',
                       'is_phonenumber_confirmed', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('phonenumber',)
    ordering = ('phonenumber',)
    filter_horizontal = ()


admin.site.register(models.BaseUser, CustomBaseUserAdmin)
admin.site.register(models.SuperUser, CustomSuperUserAdmin)
admin.site.register(models.DoctorUser, CustomDoctorUserAdmin)
admin.site.register(models.CommonUser, CustomCommonUserAdmin)
