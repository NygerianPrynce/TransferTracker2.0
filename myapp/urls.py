# myproject/myapp/urls.py

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('run_method', views.run_method, name='run_method'),
    # New URL pattern for calling findDailyTransferz
    path('run_daily_transferz', views.run_daily_transferz, name='run_daily_transferz'),  # Add this line to include the new view
    path('player_search/', views.player_search, name='player_search'),  # Add this line for player search
    path('daily_transfers/', views.daily_transfers, name='daily_transfers'),  # Add this line for daily transfers
    path('login/', views.login_view, name='login'),  # Add login view URL
    path('signup/', views.signup_view, name='signup'),  # Add signup view URL
    path('home/', views.home, name='home'),  # Add home view URL
    path('logout/', views.logout_view, name='logout'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('profile/', views.profile, name='profile'),
    path('profile/', views.profile_view, name='profile'),

]
