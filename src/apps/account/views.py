from django.contrib import messages
from django.views.generic import TemplateView, View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login as login_handler, logout as logout_handler
from django.utils.translation import gettext_lazy as _

from apps.core.utils import form_validate_err

from . import forms


class Login(TemplateView):
    template_name = 'account/login.html'
    form = forms.LoginForm
    redirect_url = reverse_lazy('account:login')

    def post(self, request):
        f = self.form(data=request.POST)

        if not form_validate_err(request, f):
            return redirect(self.redirect_url)

        data = f.cleaned_data
        username = data.get('username')
        password = data.get('password')
        remember_me = data.get('remember_me', False)

        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, _('user not found'))
            return redirect(self.redirect_url)

        login_handler(request, user)
        if not remember_me:
            request.session.set_expiry(0)

        messages.success(request, _('login successfully'))
        return redirect(user.get_dashboard_url())


class Logout(View):

    def get(self, request):
        logout_handler(request)
        return redirect('account:login')
