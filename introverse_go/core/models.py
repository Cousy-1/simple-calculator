from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name


   

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('clothes', 'Clothes'),
        ('crochets', 'Crochets'),
        ('houses', 'Houses'),
        ('books', 'Books'),
        ('cars', 'Cars'),
        ('shoes', 'Shoes'),
        ('compuers', 'Compuers'),
        ('phones', 'Phones'),
        ('Edibles', 'Edibles'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

# About Page Content
class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

# Admin Settings
class AdminSettings(models.Model):
    setting_name = models.CharField(max_length=255)
    value = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

# Chat Messages
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Contact Form Submissions
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Dashboard Statistics
class DashboardStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_orders = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    last_login = models.DateTimeField(auto_now=True)

# Database Overview (for Admin)
class DatabaseOverview(models.Model):
    table_name = models.CharField(max_length=255)
    record_count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

# Features Section
class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='features/', null=True, blank=True)

# Password Reset Requests
class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Logout Tracking
class UserLogout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# User Management
class ManagedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=[('Admin', 'Admin'), ('Customer', 'Customer'), ('Vendor', 'Vendor')])
    status = models.CharField(max_length=100, choices=[('Active', 'Active'), ('Suspended', 'Suspended')])

# Privacy Policy
class PrivacyPolicy(models.Model):
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

# User Profiles
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)

# User Settings
class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    notifications_enabled = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)

# Admin-Specific Settings
class AdminSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission_level = models.CharField(max_length=100, choices=[('SuperAdmin', 'SuperAdmin'), ('Moderator', 'Moderator')])

# Signin Logs
class SigninLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# Signup Records
class SignupLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signup_date = models.DateTimeField(auto_now_add=True)

# Terms and Conditions
class TermsOfService(models.Model):
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

# Shop Marketplace
class Homepage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')])
    ordered_at = models.DateTimeField(auto_now_add=True)
