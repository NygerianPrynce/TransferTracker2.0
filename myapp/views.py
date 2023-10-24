# myapp/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .runner import findSearchedItemz
from .runner import findDailyTransferz
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
#from .forms import SignUpForm, LoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import SignupForm
from .forms import LoginForm
from django.templatetags.static import static
import os
from django.conf import settings
import csv




# myapp/views.py

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                # Redirect to a success page or home page
                return redirect('home')  # Change 'home' to your desired URL name
            else:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to your desired page after logout

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.models import User

def signup(request):
    global new_user_id
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                email = form.cleaned_data['email']
                print(email)
                password = form.cleaned_data['password']
                print(password)
                phone_number = form.cleaned_data['phone_number']
                
                email_notifs = form.cleaned_data['email_notification']
                phone_notifs = form.cleaned_data['phone_notification']
                print(phone_number)
                
                # Check if a user with the same email already exists
                if User.objects.filter(username=email).exists():
                    form.add_error('email', 'A user with this email already exists.')
                    print("email issue")
                else:
                    # Create a new user
                    csv_file = settings.CSV_LOC + "info.csv"  

                    
                    with open(csv_file, 'r') as file:
                        csv_data = list(csv.reader(file))
                   
                   
                    if (len(csv_data) > 1):
                        new_user_id = len(csv_data)
                    else:
                        new_user_id = 1
                    
                    user = User.objects.create_user(username=email, email=email, password=form.cleaned_data['password'], first_name = new_user_id)
                    login(request, user)
                    
                    data = {
                    "id": new_user_id,
                    "email": email,
                    "phone_number": phone_number,
                    "emailNotifs": email_notifs,
                    "watchlistinfo":"",
                    "pids": "",
                    "cids": "",
                    "lids": "",
                    "phoneNotifs": phone_notifs,
                    }
                    
                    fieldnames = ["id", "email", "phone_number", "emailNotifs", "watchlistinfo", "pids", "cids", "lids", "phoneNotifs"]

                    with open(csv_file, mode='a', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='|')

                    # Write headers if the file is empty
                        if file.tell() == 0:
                            writer.writeheader()

                        # Write the data for each user
                        writer.writerow(data)
                        #writer.writerow(data)

                    print(f'CSV file "{csv_file}" has been updated.')

                    
                    
                    
                    return redirect('home')
            else:
                form.add_error('confirm_password', 'Passwords do not match')
                print("password")
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def player_search(request):
    user_id = request.user.first_name
    return render(request, 'player_search.html', {"user_id":user_id})

def daily_transfers(request):
    user_id = request.user.first_name
    return render(request, 'daily_transfers.html', {"user_id":user_id})

def watchlist(request):
    user_id = request.user.first_name
    return render(request, 'watchlist.html', {"user_id":user_id})

def profile(request):
    user_id = request.user.first_name
    return render(request, 'profile.html', {"user_id":user_id})

def run_method(request):
    try:
        # Get the search term from the request
        search_term = request.GET.get('search_term', '')
        
        # Call the findSearchedItemz function with the search term
        result = findSearchedItemz(search_term)
        return JsonResponse({'status': 'success', 'result': result})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
        
def run_daily_transferz(request):
    try:
        # Get the search term from the request
        pids = request.GET.get('pids', '').split(",")
        cids = request.GET.get('cids', '').split(",")
        lids = request.GET.get('lids', '').split(",")
        
        # Call the findSearchedItemz function with the search term
        result = findDailyTransferz(pids, cids, lids)
        print(result)
        return JsonResponse({'status': 'success', 'result': result})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
#findDailyTransferz(pids, cids, lids)
from django.shortcuts import render, redirect
from django.http import HttpResponse

def profile_view(request):
    if request.method == "POST":
        # Handle form submission as shown in the previous answers
        full_name = request.POST.get("full_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

    # Render the "profile.py" template and pass the form data as context variables
    context = {
        'full_name': request.POST.get("full_name"),
        'username': request.POST.get("username"),
        'email': request.POST.get("email"),
        'password1': request.POST.get("password1"),
        'password2': request.POST.get("password2"),
    }
    
    return render(request, 'profile.html', context)

from django.http import JsonResponse

def update_csv_file(request):
    if request.method == 'POST':
        modified_csv = request.POST.get('modifiedCSV')

        if modified_csv:
            csv_file = settings.CSV_LOC + "info.csv" 
            with open(csv_file, 'w') as file:
                file.write(modified_csv)

            return JsonResponse({'message': 'CSV file has been updated successfully.'})
        else:
            return JsonResponse({'error': 'No modified CSV data received.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
