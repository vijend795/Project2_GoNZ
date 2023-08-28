from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import NewUser
from django.contrib.auth.models import Group
from django.http import HttpResponse
from tours.models import Tour
from django.db.models import Count

# Custom user group checkers
def is_admin(user):
    return user.groups.filter(name='Administrator').exists()
    

def is_management(user):
    return user.groups.filter(name='Management').exists()

def is_agent(user):
    return user.groups.filter(name='Agent').exists()

@login_required(login_url='/accounts/login')
def users_list(request):
    if is_admin(request.user):
        users = NewUser.objects.all()
        type="Admin"
    elif is_management(request.user):
        users = NewUser.objects.filter(groups__name='Agent')
        type="Manager"
    elif is_agent(request.user):
        users = NewUser.objects.filter(pk=request.user.pk, department='Agent')
        
        type="Agent"
    else:
        users = []
        
    if is_management(request.user) :
        users = users | NewUser.objects.filter(pk=request.user.pk)
    
    context = {
        'users_list': users,
        'type':type,
    }
    return render(request, 'users_list.html', context)

@login_required   
def user_details(request, agent_id):
    agent = get_object_or_404(NewUser, pk=agent_id)
    agent_groups = ', '.join([group.name for group in agent.groups.all()])
    tours=Tour.objects.filter(agent=agent_id)
    logged_in_user_id = request.session.get('_auth_user_id')
    
    if is_admin(request.user) or (is_management(request.user) and (agent.department == 'Agent' or request.user.pk == agent.pk)) or (is_agent(request.user) and request.user.pk == agent.pk):
        context = {
            'user': agent,
            'user_groups': agent_groups,
            'tours':tours,
            'logged_in_user_id': logged_in_user_id,
        }
        return render(request, 'user_details.html', context)
    else:
        # Return an error message or redirect to unauthorized page
        # return render(request, 'unauthorized.html')  # Example: Create an unauthorized.html template
        return HttpResponse("you dont have access to this page")
