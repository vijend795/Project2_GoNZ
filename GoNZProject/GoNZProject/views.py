from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.
def home(request):
    
    return render(request,'index.html')



def login_view(request):
    # Your login logic here
    
    # Set the session variable to store the username
    request.session['logged_in_username'] = request.user.username
    request.session['logged_in_user_id'] = request.user.id

    
    return redirect('profile')  # Redirect to the profile page or another appropriate page
