from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import VendorSignupForm, UserSignupForm, VendorLoginForm, UserLoginForm, TravelPackageForm
from .models import TravelPackage
from django.utils import timezone


def main_page(request):
    return render(request, 'main_page.html')


def vendor_signup(request):
    form = VendorSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('vendor_dashboard')
    return render(request, 'vendor_signup.html', {'form': form})


def user_signup(request):
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)
        return redirect('user_dashboard')
    return render(request, 'user_signup.html', {'form': form})


def vendor_login(request):
    form = VendorLoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            return redirect('vendor_dashboard')
    return render(request, 'vendor_login.html', {'form': form})


def user_login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(request, user)
            return redirect('user_dashboard')
    return render(request, 'user_login.html', {'form': form})


@login_required
def vendor_dashboard(request):
    form = TravelPackageForm(request.POST, request.FILES or None)
    if form.is_valid():
        package = form.save(commit=False)
        package.vendor = request.user
        package.save()
        return redirect('vendor_dashboard')
    return render(request, 'vendor_dashboard.html', {'form': form})


@login_required
def user_dashboard(request):
    packages = TravelPackage.objects.filter(is_approved=True, tour_date__gte=timezone.now())
    return render(request, 'user_dashboard.html', {'packages': packages})


def vendor_logout(request):
    logout(request)
    return redirect('main_page')


def user_logout(request):
    logout(request)
    return redirect('main_page')
