# myproject/myapp/urls.py

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', views.index, name='index'),
    path('run_method', views.run_method, name='run_method'),
    # New URL pattern for calling findDailyTransferz
    path('run_daily_transferz', views.run_daily_transferz, name='run_daily_transferz'),  # Add this line to include the new view
    path('player_search/', views.player_search, name='player_search'),  # Add this line for player search
    path('daily_transfers/', views.daily_transfers, name='daily_transfers'),  # Add this line for daily transfers
    path('login/', views.login_view, name='login'),  # Add login view URL
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),  # Add home view URL
    path('logout/', views.logout_view, name='logout'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('profile/', views.profile, name='profile'),
    path('profile/', views.profile_view, name='profile'),
    path('update-csv/', views.update_csv_file, name='update_csv_file'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),



]
