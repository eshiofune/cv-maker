from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("logout/", views.logout, name='logout'),
    path('createcv/', views.createcv, name='createcv'),
    path('profileform/', views.profileform, name='profileform'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('profile<int:id>/', views.profile, name='profile'),
    path('temp<int:id>/', views.temp, name='temp'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
