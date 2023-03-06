"""trackermis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView,PasswordResetDoneView
from django.conf.urls.static import static
from django.urls import path, include
from leads.views import landin_page, LandingPageView, SignupView

admin.site.site_header = "Tracker MIS Admin"
admin.site.site_title = "Tracker MIS Admin Portal"
admin.site.index_title = "Welcome to Tracker MIS Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path("leads/", include('leads.urls', namespace="leads")),
    path("agents/", include('agent.urls', namespace="agent")),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("reset-password/", PasswordResetView.as_view(), name='reset-password'),
    path("reset-password-done/", PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("signup/", SignupView.as_view(), name='signup'),
    path("inventory/", include('inventory.urls', namespace="inventory"))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)