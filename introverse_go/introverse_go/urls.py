from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from core import views  
from django.urls import path
from . import views

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

   
    
    path('admin-login-signup/', views.admin_login_signup, name='admin_login_signup'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-signup/', views.admin_signup, name='admin_signup'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.admin_logout, name='logout'),





    # Core Views
    path("", views.home, name="home"),
    path("homepage/", views.homepage, name="home"),
    path("about/", views.about, name="about"),
    path("features/", views.features, name="features"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("profile/", views.profile, name="profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("chat/", views.chat, name="chat"),

    # Marketplace
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),

    # Authentication
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("logout/", auth_views.LogoutView.as_view(next_page="signin"), name="logout"),

    # Password Reset
    path("forgot-password/", auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="forgot_password"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),

    # Static Pages
    path("admin-page/", TemplateView.as_view(template_name="admin.html"), name="admin_page"),
    path("db-overview/", TemplateView.as_view(template_name="db_overview.html"), name="db_overview"),
    path("manage-users/", TemplateView.as_view(template_name="manage_users.html"), name="manage_users"),
    path("privacy-policy/", TemplateView.as_view(template_name="privacy_policy.html"), name="privacy_policy"),
    path("settings/", TemplateView.as_view(template_name="settings.html"), name="settings"),
    path("settings-admin/", TemplateView.as_view(template_name="settings_admin.html"), name="settings_admin"),
    path("terms-of-service/", TemplateView.as_view(template_name="terms.html"), name="terms"),

    # MPesa API
    path("mpesa/stk-push/", views.mpesa_stk_push, name="mpesa_stk_push"),
]

# Static and Media Files (For Development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
