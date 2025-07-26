# Placeholder views for Withdraw, Deposit, and Report
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render


@login_required
def withdraw_view(request):
    return render(request, 'accounts/withdraw.html')


@login_required
def deposit_view(request):
    return render(request, 'accounts/deposit.html')


@login_required
def report_view(request):
    return render(request, 'accounts/report.html')


# Simple profile view


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Registration successful!')
        return HttpResponseRedirect(self.get_success_url())
