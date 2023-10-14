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
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
# myapp/views.py

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(username=phone, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/users/home')
        else:
            error = " Sorry! Phone Number and Password didn't match, Please try again ! "
            return render(request, 'login/index.html',{'error':error})
    else:
        return render(request, 'login/index.html')
    '''
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("User logged in:", user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    '''


def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to your desired page after logout

def signup_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'signup.html', { 'form': form})
    '''
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass_1 = request.POST.get('password1')
        pass_2 = request.POST.get('password2')
        if pass_1 == pass_2:
             user = User.objects.create_user(
                                              username=phone,
                                              email=email,
                                              password=pass_1,
                                             )
             return HttpResponseRedirect("/")
        else:
             error = " Password Mismatch "
             return render(request, 'login/signup.html',{"error":error})
        
    else:
         return render(request, 'login/signup.html')    
        
    '''    
    '''
    
    
    form = UserRegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        print("User signed up:", username)
        return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})

    '''

@login_required
def home(request):
    return render(request, 'home.html')

def player_search(request):
    return render(request, 'player_search.html')

def daily_transfers(request):
    return render(request, 'daily_transfers.html')

def watchlist(request):
    return render(request, 'watchlist.html')

def profile(request):
    return render(request, 'profile.html')

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




