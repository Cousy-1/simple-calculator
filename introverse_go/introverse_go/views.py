from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def features(request):
    return render(request, "features.html")

def contact(request):
    return render(request, "contact.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")  # Redirect to sign-in page after successful signup
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")  # Redirect to dashboard after successful signin
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("signin")  # Redirect to sign-in page after logout

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms_of_service(request):
    return render(request, "terms.html")
