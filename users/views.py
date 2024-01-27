from django.contrib.auth import login, authenticate

# uses custom form instead of UserCreationForm
from .forms import UserRegisterForm

# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def register(request):
    """Displays the registration page"""
    PROUT
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Login automatically
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect("search:home")
    else:
        form = UserRegisterForm()
    return render(
        request, "register.html", {"form": form}
    )  # form as a context to be used in template


@login_required  # only allows this page to logged_in users
def account(request):
    """Displays the account page when a user is logged in"""
    return render(request, "account.html")

