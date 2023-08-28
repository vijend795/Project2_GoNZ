from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Tour
from django.contrib.auth.models import Group
from django.http import HttpResponse

# Custom user group checkers


# Create your views here.
def tours_list(request):
    # print(request.session.items())
    tour_list=Tour.objects.all()
    logged_in_user_id = request.session.get('_auth_user_id')
    # print(logged_in_user_id )

    context = {
        'tour_list': tour_list,
        'logged_in_user_id': logged_in_user_id,
    }
    return render(request, 'tour_list.html', context)


def tour_details(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    logged_in_user_id = request.session.get('_auth_user_id')
    context = {
            'tour': tour,
            'logged_in_user_id': logged_in_user_id,
        }
    return render(request, 'tour_details.html', context)
   