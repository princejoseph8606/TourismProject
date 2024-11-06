from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import VendorSignupForm, UserSignupForm, VendorLoginForm, UserLoginForm, TravelPackageForm
from .models import TravelPackage
from django.utils import timezone
from django.contrib import messages

def main_page(request):
    packages = TravelPackage.objects.filter(is_approved=True, tour_date__gte=timezone.now())
    return render(request, 'main_page.html', {'packages': packages})
    #return render(request, 'main_page.html')


def vendor_signup(request):
    form = VendorSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        packages = TravelPackage.objects.filter(is_approved=True, tour_date__gte=timezone.now())
        return render(request, 'main_page.html', {'packages': packages})
        #login(request, user)
        #return redirect('vendor_dashboard')
    return render(request, 'vendor_signup.html', {'form': form})


def user_signup(request):
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        #login(request, user)
        packages = TravelPackage.objects.filter(is_approved=True, tour_date__gte=timezone.now())
        return render(request, 'main_page.html', {'packages': packages})
        #return redirect('user_dashboard')
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
            packages = TravelPackage.objects.filter(vendor=user)
            package_names = [package.package_name for package in packages]
            return render(request, 'vendor_home.html', {'package_names': package_names})
            #return redirect('vendor_home')
            #return redirect('vendor_dashboard')
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
def vendor_home(request):
    return render(request, 'vendor_home.html')

@login_required
def vendor_dashboard(request):
    form = TravelPackageForm(request.POST, request.FILES or None)
    if form.is_valid():
        package = form.save(commit=False)
        package.vendor = request.user
        package.save()
        return redirect('vendor_home')
        #return redirect('vendor_dashboard')
    return render(request, 'vendor_dashboard.html', {'form': form})
@login_required
def edit_package(request, package_id):
    package = get_object_or_404(TravelPackage, id=package_id, vendor=request.user)
    form = TravelPackageForm(request.POST or None, request.FILES or None, instance=package)
    if form.is_valid():
        form.save()
        messages.success(request, "Package updated successfully.")
        return redirect('vendor_home')
    return render(request, 'edit_package.html', {'form': form, 'package': package})

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
