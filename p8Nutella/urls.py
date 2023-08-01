"""p8Nutella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views
from django.views.static import serve
from p8Nutella import settings
# from django.conf import settings as setting
from django.conf.urls.static import static
# from . import views


urlpatterns = [
    # Other App Views
    path("", include("search.urls")),

    # Custom views
    path("register/", users_views.register, name="register"),
    path("account", users_views.account, name="account"),
    # Django Views
    path("login/",  auth_views.LoginView.as_view
         (template_name="login.html"), name="login"),
    path("logout/",  auth_views.LogoutView.as_view
         (template_name="logout.html"), name="logout"),
    # path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT, }),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
