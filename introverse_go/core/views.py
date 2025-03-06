from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib import messages

# M-Pesa STK Push

def mpesa_stk_push(request):
    return JsonResponse({"message": "STK push initiated"})

# Core Views
def home(request):
    products = Product.objects.all()
    return render(request, "homepage.html", {"products": products})

def homepage(request):
    return render(request, "homepage.html")
def about(request):
    return render(request, "about.html")

def features(request):
    return render(request, "features.html")

def contact(request):
    return render(request, "contact.html")

def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})

# Marketplace Views
CATEGORY_CHOICES = [
    ('clothes', 'Clothes'),
    ('crochets', 'Crochets'),
    ('houses', 'Houses'),
    ('books', 'Books'),
    ('cars', 'Cars'),
    ('shoes', 'Shoes'),
    ('computers', 'Computers'),
    ('phones', 'Phones'),
    ('edibles', 'Edibles'),
]

def marketplace(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products, 'CATEGORY_CHOICES': CATEGORY_CHOICES})

def add_to_cart(request):
/*************  ✨ Codeium Command ⭐  *************/
"""
Handles the display of products available for adding to the shopping cart.

Renders the 'add_to_cart.html' template with a list of all products 
retrieved from the database.

Args:
    request: The HTTP request object from the client.

Returns:
    A rendered HTML page displaying available products for the cart.
"""

/******  9e874ad4-309c-40a7-b725-17c50b7f0e6f  *******/
    products = Product.objects.all()
    return render(request, "add_to_cart.html", {"products": products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect("marketplace")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})

# Authentication Views
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {"form": form})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'admin_login_signup.html')

def admin_login_signup(request):
    return render(request, 'admin_login_signup.html')  # Ensure this template exists

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'admin_login_signup.html')

def admin_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully")
            return redirect('admin_login')
    return render(request, 'admin_login_signup.html')

def admin_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    user_count = User.objects.count()
    return render(request, 'admin_dashboard.html', {'user_count': user_count})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

from django.urls import path
from . import views

urlpatterns = [
    path('admin-login-signup/', views.admin_login_signup, name='admin_login_signup'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-signup/', views.admin_signup, name='admin_signup'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout, name='logout'),
]

def logout_view(request):
    logout(request)
    return render(request, "logout.html")

# Password Reset
def forgot_password(request):
    return render(request, "forgot_password.html")

# Admin & Dashboard
def admin_page(request):
    return render(request, "admin.html")

def dashboard(request):
    return render(request, "dashboard.html")

def db_overview(request):
    return render(request, "db_overview.html")

def manage_users(request):
    return render(request, "manage_users.html")

# User Settings & Profile
def profile(request):
    return render(request, "profile.html")

def settings(request):
    return render(request, "settings.html")

def settings_admin(request):
    return render(request, "settings_admin.html")

# Static Pages
def chat(request):
    return render(request, "chat.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")

def terms_of_service(request):
    return render(request, "terms.html")
