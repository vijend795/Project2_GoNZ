from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'

def user_profile(request):
    logged_in_user = request.user

    

    user_groups = ', '.join([group.name for group in logged_in_user.groups.all()])
    user = {
        'user': logged_in_user,
        'user_groups': user_groups,
    }
    # Store the logged-in username in the session
    request.session['logged_in_username'] = logged_in_user.username
    request.session['logged_in_user_group'] = user_groups
    return render(request, 'registration/profile.html', user)

