from django.urls import path, re_path
from .views import homepage, signup , rooms , joinRoom
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('rooms/', rooms, name='rooms'),
    path('rooms/<slug:slug>/', joinRoom , name='joinRoom'),
]